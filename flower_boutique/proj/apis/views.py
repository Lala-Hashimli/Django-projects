from rest_framework.views import APIView, Response, status
from flowers.models import Flowers, Category
from flowers.serializers import FlowersSerializers
from django.views.generic import ListView as LV
from .utils import send_email_notification
from drf_yasg.utils import swagger_auto_schema


class TestFront(LV):
    model = Flowers
    template_name = "index.html"
    context_object_name = "products"
    
    def get_queryset(self):
        queryset = Flowers.objects.filter(status=Flowers.APPROVED)

        category_id = self.request.GET.get("category")
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["selected_category"] = self.request.GET.get("category")
        return context


class FlowersAPIViews(APIView):
    def get(self, request):
        flowers = Flowers.objects.filter(status=Flowers.APPROVED)
        serializers = FlowersSerializers(flowers, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=FlowersSerializers)
    def post(self, request):
        data = request.data
        serializer = FlowersSerializers(data=data)

        if serializer.is_valid():
            flower = serializer.save()
            send_email_notification(flower)
            return Response({"message": "Flower is created successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlowersDetailsAPIViews(APIView):
    def get(self, request, flower_id):
        flower = Flowers.objects.filter(pk=flower_id, status=Flowers.APPROVED).first()
        if not flower:
            return Response(
                {"error": "Product is pending approved"}, 
                status=status.HTTP_404_NOT_FOUND)

        serializer = FlowersSerializers(flower)
        return Response(serializer.data, status=status.HTTP_200_OK)
        