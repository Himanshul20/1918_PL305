from . import views
from django.urls import path


urlpatterns = [

    path('BookingForm', views.book, name='BookingForm'),
    path('show', views.show, name='show'),
    path('dash', views.show, name='show'),

]
