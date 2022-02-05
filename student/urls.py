from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_list, name='create_list'),
    path('<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]