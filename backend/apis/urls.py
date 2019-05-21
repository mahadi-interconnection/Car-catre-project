from django.conf.urls import (
    url,
    include
)
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    ManufactorCreateView,
    ManufactorDetailsView,
    ShowroomCreateView,
    ShowroomDetailsView,
    UserCreateView,
    UserDetailsView,
    CarCreateView,
    CarDetailsView,
    ShowroomWiseView,
)

urlpatterns = {
    url(r'^manufactor/$',
        ManufactorCreateView.as_view(), name="create_manufactor"),
    url(r'^manufactor/(?P<pk>[0-9]+)/$',
        ManufactorDetailsView.as_view(), name="details_manufactor"),
    url(r'^showrooms/$',
        ShowroomCreateView.as_view(), name="create_showroom"),
    url(r'^showrooms/(?P<pk>[0-9]+)/$',
        ShowroomDetailsView.as_view(), name="details_showroom"),
    url(r'^users/$',
        UserCreateView.as_view(), name="create_user"),
    url(r'^users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="details_user"),
    url(r'^cars/$',
        CarCreateView.as_view(), name="create_car"),
    url(r'^cars/(?P<pk>[0-9]+)/$',
        CarDetailsView.as_view(), name="details_car"),
    url(r'^showroomwisecar/$',
        ShowroomWiseView.as_view(), name="car_showroom"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
