from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainee_list, name='trainee_list'),
    path('add/', views.add_trainee, name='add_trainee'),
    path('<int:id>/', views.trainee_detail, name='trainee_detail'),
    path('delete/<int:id>/', views.delete_trainee, name='delete_trainee'),
]