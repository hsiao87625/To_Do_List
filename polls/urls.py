from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_mission', views.new_mission, name='new_mission'),
    ]