from django.shortcuts import render

from rest_framework import (
    viewsets,
    generics
)
from .models import (
    Manufactor,
    Showroom,
    User,
    Car,
)

from .serializers import (
    ManufactorSerializer,
    ShowroomSerializer,
    UserSerializer,
    CarSerializer,
    CarSerializerBasic,
    ShowroomWiseCarSerializer,
    CarLiteSerializer,
    
)    


# Create your views here.

# Manufactor
class ManufactorCreateView(generics.ListCreateAPIView):
    
    queryset = Manufactor.objects.all()
    serializer_class = ManufactorSerializer

    def perform_create(self, serializer):
        serializer.save()

class ManufactorDetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Manufactor.objects.all()
    serializer_class = ManufactorSerializer        


# Showroom
class ShowroomCreateView(generics.ListCreateAPIView):
    
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer

    def perform_create(self, serializer):
        serializer.save()

class ShowroomDetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer        


#User
class UserCreateView(generics.ListCreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer 


#Car
class CarCreateView(generics.ListCreateAPIView):
    
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_serializer_class(self, *args, **kwargs):
        # return CarSerializer
        if self.request.method == 'GET':
            return CarSerializer
        return CarSerializerBasic 

    
    def perform_create(self, serializer):
        serializer.save()


class CarDetailsView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_serializer_class(self, *args, **kwargs):
        # return CarSerializer
        if self.request.method == 'GET':
            return CarSerializer
        return CarSerializerBasic 

# Showroomwise_car

class ShowroomWiseView(generics.ListAPIView):
    serializer_class = ShowroomWiseCarSerializer
    def get_queryset(self):
        return Showroom.objects.all()
    