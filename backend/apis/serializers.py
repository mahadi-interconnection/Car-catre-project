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




class CarLiteSerializer(serializers.ModelSerializer):
    # showroom = ShowroomSerializer()
    manufactor = ManufactorSerializer()
    class Meta:
        model = Car
        fields = ('id','image','mileage','model','showroom','manufactor')


class CarSerializer(CarLiteSerializer):
    showroom = ShowroomSerializer()
    

class ShowroomWiseCarSerializer(serializers.ModelSerializer):
    car_showroom=CarLiteSerializer(many=True)
    class Meta:
        model = Showroom
        fields = ('id','name', 'car_showroom')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email')

# added
class CarSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id','image','mileage','model','showroom','manufactor')        