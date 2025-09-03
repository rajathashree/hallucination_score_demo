from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey_chat, name='survey_form'),
]