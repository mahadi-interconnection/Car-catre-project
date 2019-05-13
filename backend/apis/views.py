from django.shortcuts import render
from rest_framework import viewsets
from .models import Manufactor,Showroom,Car
from .serializers import ManufactorSerializer,CarSerializer,ShowroomSerializer

# Create your views here.

class ManufactorView(viewsets.ModelViewSet):
    queryset = Manufactor.objects.all()
    serializer_class = ManufactorSerializer

class ShowroomView(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer

class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer    