from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('events', views.events_page, name="events"),
    path('importance', views.importance_page, name="importance"),
    path('introduction', views.intro_page, name="introduction"),
    path('members', views.members_page, name="members"),
    path('thankyou', views.thankyou, name="thankyou"),
    path('registration_page', views.mulitstepform.as_view(), name="registration_page"),
    # path('registration_2/<str:form>/', views.registration_page_2, name="registration_2"),
    # path('registration_3', views.registration_page, name="registration_3"),
    path('feedback', views.feedback_page, name="feedback"),
    path('particular_eve/<int:eveid>/', views.particular_eves, name="particular_eve"),
]