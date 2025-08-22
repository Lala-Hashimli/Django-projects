from rest_framework import serializers
from .models import Flowers

class FlowersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flowers
        fields = '__all__'