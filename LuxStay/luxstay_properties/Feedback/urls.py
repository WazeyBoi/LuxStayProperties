from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('create/', views.feedback_create, name='feedback_create'),
    path('update/<int:pk>/', views.feedback_update, name='feedback_update'),
    path('delete/<int:pk>/', views.feedback_delete, name='feedback_delete'),
]
