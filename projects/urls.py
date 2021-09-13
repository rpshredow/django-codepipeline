from django.urls import path
from . import views

urlpatterns = [
    path('terrain/', views.terrain, name='projects-terrain'),
    path('cluster/', views.cluster, name='projects-cluster'),
]