from rest_framework import serializers
from .models import Car,Showroom,Manufactor,User

class ManufactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufactor
        fields = ('id' , 'name')

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('image','mileage','model','showroom','manufactor')

class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ('id','name')