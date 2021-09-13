from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
#from .models import Post
    
def terrain(request):
    return render(request, 'projects/terrain.html', {'title': '3D Terrain App'})

def cluster(request):
    return render(request, 'projects/cluster.html', {'title': 'Raspberry Pi Cluster'})

def thesis(request):
    return render(request, 'projects/thesis.html', {'title': 'Masters Thesis'})

def fpgann(request):
    return render(request, 'projects/fpgann.html', {'title': 'FPGA Neural Network'})