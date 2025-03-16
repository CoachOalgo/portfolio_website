# line_logic_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visualize/<int:pk>/', views.visualize, name='visualize'),
    path('api/graph/<int:pk>/', views.get_graph_data, name='get_graph_data'),
]