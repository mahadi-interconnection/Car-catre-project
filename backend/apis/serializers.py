from rest_framework import serializers
from .models import (
                     Manufactor ,
                     Showroom,
                     User,
                     Car,
                     )


class ManufactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufactor
        fields = ('id' , 'name')

class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ('id','name','logo')           

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email')   


#Car

class CarSerializer(serializers.ModelSerializer):
    showroom = ShowroomSerializer()
    manufactor = ManufactorSerializer()
    class Meta:
        model = Car
        fields = ('id','image','mileage','model','status','transmission','propellant','horse_power','showroom','manufactor') 


class CarSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id','image','mileage','model','status','transmission','propellant','horse_power','showroom','manufactor')      


#Showroomwise_car

class CarLiteSerializer(serializers.ModelSerializer):
    # showroom = ShowroomSerializer()
    # manufactor = ManufactorSerializer()
    class Meta:
        model = Car
        fields = ('id','image','mileage','model','status','transmission','propellant','horse_power','showroom','manufactor')


class ShowroomWiseCarSerializer(serializers.ModelSerializer):
    # car_showroom is the reference to car from showroom
    car_showroom=CarLiteSerializer(many=True)
    class Meta:
        model = Showroom
        fields = ('id','name', 'car_showroom')            