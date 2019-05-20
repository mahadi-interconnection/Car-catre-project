from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import (
    Manufactor,
    Showroom,
    User,
    Car,
)
# from django.db import models

class ManufactorSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    name = serializers.CharField(validators=[UniqueValidator(queryset=Manufactor.objects.all())])
    class Meta:
        model = Manufactor
        fields = ('id', 'name')
    
class ShowroomSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[UniqueValidator(queryset=Showroom.objects.all())])
    class Meta:
        model = Showroom
        fields = ('id', 'name', 'logo')


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ('id', 'name', 'email')


class CarSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'image', 'mileage', 'model', 'status', 'transmission',
                  'propellant', 'horse_power', 'showroom', 'manufactor')


# Showroomwise_car

class CarLiteSerializer(serializers.ModelSerializer):
    # showroom = ShowroomSerializer()
    # manufactor = ManufactorSerializer()
    class Meta:
        model = Car
        fields = ('id', 'image', 'mileage', 'model', 'status', 'transmission',
                  'propellant', 'horse_power', 'showroom', 'manufactor')

# Car

class CarSerializer(CarLiteSerializer):
    showroom = ShowroomSerializer()
    manufactor = ManufactorSerializer()


class ShowroomWiseCarSerializer(serializers.ModelSerializer):
    # car_showroom is the reference to car from showroom
    car_showroom = CarLiteSerializer(many=True)

    class Meta:
        model = Showroom
        fields = ('id', 'name', 'car_showroom')
