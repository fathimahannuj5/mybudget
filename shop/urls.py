from django.urls import path,include
from . import views
urlpatterns=[
    path('shopping/',views.MyShop,name='shopping'),
   ]
