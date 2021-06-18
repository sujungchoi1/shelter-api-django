from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ShelterSerializer
from .models import Shelter

class ShelterViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = Shelter.objects.all().order_by('name')
    serializer_class = ShelterSerializer