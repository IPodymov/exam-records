from django.urls import path
from . import views

urlpatterns = [
    path('exam/', views.exam_list, name='exam_list'),
    path('exam/add/', views.exam_create, name='exam_create'),
]
