from rest_framework import serializers
from .models import studentClass
class stuSerializer(serializers.ModelSerializer):
       class Meta:
         model=studentClass
         fields=['name','grade']