from django.shortcuts import render
from .models import Flowers, Category

def home(request):
    category_id = request.GET.get("category")
    flowers = Flowers.objects.filter(status=Flowers.APPROVED)

    if category_id:
        flowers = flowers.filter(category_id=category_id)


    categories = Category.objects.all()

    api = {"products": flowers,
           "categories": categories,
           "selected_category": category_id or '',
           "request": request}

    
    return render(request, "flowers/index.html", api)
