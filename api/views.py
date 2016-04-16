from django.shortcuts import render
from rest_framework import generics
from .serializers import *

# Create your views here.
class BicycleView(generics.ListCreateAPIView):
    queryset = Bicycle.objects.all()
    serializer_class = DefaultBicycleSerializer

class BicycleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bicycle.objects.all()
    serializer_class = DefaultBicycleSerializer