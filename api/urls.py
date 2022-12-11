from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import BakeryViewSet,RegisterUser,CustomerViewSet
from .views import *




router=routers.DefaultRouter()
router.register(r'bakery',BakeryViewSet)
router.register(r'customer',CustomerViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('register/',RegisterUser.as_view()),
    
]
