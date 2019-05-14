from django.test import TestCase

# Create your tests here.
import json
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Manufactor,Showroom,Car,User
from .serializers import ManufactorSerializer,CarSerializer,ShowroomSerializer,UserSerializer,CarSerializerBasic

# Create your tests here.

class CarDetailsTestCase(TestCase):
    def test_get_all_car(self):
        new_client = APIClient()
        res = new_client.get('/cars/', format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

class ShowroomDetailsTestCase(TestCase):
    def test_get_all_car(self):
        new_client = APIClient()
        res = new_client.get('/showrooms/', format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

class ManufactorDetailsTestCase(TestCase):
    def test_get_all_car(self):
        new_client = APIClient()
        res = new_client.get('/manufactor/', format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

class UserDetailsTestCase(TestCase):
    def test_get_all_car(self):
        new_client = APIClient()
        res = new_client.get('/users/', format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
