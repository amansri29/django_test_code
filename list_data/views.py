from rest_framework import generics
from django.shortcuts import render


from .models import ListData
from .serializers import ListDataSerializer

# Create your views here
class DataList(generics.ListCreateAPIView):
    queryset = ListData.objects.all()
    serializer_class = ListDataSerializer
    