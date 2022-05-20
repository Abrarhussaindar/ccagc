from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('events', views.events_page, name="events"),
    path('importance', views.importance_page, name="importance"),
    path('introduction', views.intro_page, name="introduction"),
    path('members', views.members_page, name="members"),
    path('registration', views.registration_page, name="registration"),
]