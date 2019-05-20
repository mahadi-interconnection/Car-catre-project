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
        ManufactorCreateView.as_view(), name="create"),
    url(r'^manufactor/(?P<pk>[0-9]+)/$',
        ManufactorDetailsView.as_view(), name="details"),
    url(r'^showrooms/$',
        ShowroomCreateView.as_view(), name="create"),
    url(r'^showrooms/(?P<pk>[0-9]+)/$',
        ShowroomDetailsView.as_view(), name="details"),
    url(r'^users/$',
        UserCreateView.as_view(), name="create"),
    url(r'^users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="details"),
    url(r'^cars/$',
        CarCreateView.as_view(), name="create"),
    url(r'^cars/(?P<pk>[0-9]+)/$',
        CarDetailsView.as_view(), name="details"),
    url(r'^showroomwisecar/$',
        ShowroomWiseView.as_view(), name="car_showroom"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
