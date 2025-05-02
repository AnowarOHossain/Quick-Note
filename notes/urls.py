from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_note, name='create'),
    path('update/<int:pk>/', views.update_note, name='update'),
    path('delete/<int:pk>/', views.delete_note, name='delete'),
]