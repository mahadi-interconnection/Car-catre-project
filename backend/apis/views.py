from django.shortcuts import render
from rest_framework import (
    viewsets,
    generics
)
from .models import Manufactor,Showroom,Car,User
from .serializers import (
    ManufactorSerializer,
    CarSerializer,
    ShowroomSerializer,
    UserSerializer,
    CarSerializerBasic,
    ShowroomWiseCarSerializer
)    


# Create your views here.

class ManufactorView(viewsets.ModelViewSet):
    queryset = Manufactor.objects.all()
    serializer_class = ManufactorSerializer

class ShowroomView(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer

class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    # serializer_class = CarSerializer 

    def get_serializer_class(self, *args, **kwargs):
        # return CarSerializer
        if self.request.method == 'GET':
            return CarSerializer
        return CarSerializerBasic 
       

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShowroomWiseView(generics.ListAPIView):
    serializer_class = ShowroomWiseCarSerializer
    def get_queryset(self):
        return Showroom.objects.all()

        
