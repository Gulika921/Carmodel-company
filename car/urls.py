from django.urls import path, include
from car.views import (
    CarListView, CarDetailView,
    CarCreateView, CarModelListView,
    CarModelDetailView, CarModelCreateView,
    CompanyListView, CompanyCreateView,
    CompanyDetailView,
)

urlpatterns = [
    path("car/", CarListView.as_view(), name="car-list"),
    path("car/create", CarCreateView.as_view(), name="car-create"),
    path("car/<int:pk>", CarDetailView.as_view(), name="car-detail"),
    path('car_model/', CarModelListView.as_view(), name='car_model-list'),
    path("car_model/create", CarModelCreateView.as_view(), name="car_model-create"),
    path("car_model/<int:pk>", CarModelDetailView.as_view(), name="car_model-detail"),
    path('company/', CompanyListView.as_view(), name='company-list'),
    path("company/create", CompanyCreateView.as_view(), name="company-create"),
    path("company/<int:pk>", CompanyDetailView.as_view(), name="company-detail"),

]
