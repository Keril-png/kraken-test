from rest_framework import serializers
from .models import Rec


class RecSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rec
        fields = '__all__'