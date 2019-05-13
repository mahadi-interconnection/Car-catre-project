# from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('cars',views.CarView)
router.register('showrooms',views.ShowroomView)
router.register('manufactor',views.ManufactorView)

urlpatterns = [
    path('', include(router.urls))
]
