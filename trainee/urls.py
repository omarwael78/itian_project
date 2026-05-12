from django.urls import path
from . import views

urlpatterns = [
    path('', views.TraineeListView.as_view(), name='trainee_list'),
    path('add/', views.TraineeCreateView.as_view(), name='add_trainee'),
    path('<int:id>/', views.TraineeDetailView.as_view(), name='trainee_detail'),
    path('delete/<int:id>/', views.TraineeDeleteView.as_view(), name='delete_trainee'),
]