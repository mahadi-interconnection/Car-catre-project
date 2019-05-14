from rest_framework import serializers
from .models import Car,Showroom,Manufactor,User

class ManufactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufactor
        fields = ('id' , 'name')

class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ('id','name')        

class CarSerializer(serializers.ModelSerializer):
    showroom = ShowroomSerializer()
    class Meta:
        model = Car
        fields = ('id','image','mileage','model','showroom','manufactor')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email')