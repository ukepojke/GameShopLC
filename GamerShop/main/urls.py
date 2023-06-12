from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('about/',about),
    path('product/',product),
    path('video/',video),
    path('remot/',remot),
    path('contact/',contact),
    path('product/<int:id>',product_detail),
]