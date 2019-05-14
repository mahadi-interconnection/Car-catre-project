# from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('cars',views.CarView)
router.register('showrooms',views.ShowroomView)
# router.register('showrooms_wise_car',views.ShowroomWiseView)
router.register('manufactor',views.ManufactorView)
router.register('showroomwisecars',views.UserView)
router.register('users',views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path(r'showrooms_wise_car/', views.ShowroomWiseView.as_view(), name='user-list')

]
