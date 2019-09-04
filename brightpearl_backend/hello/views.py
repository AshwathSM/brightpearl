from django.shortcuts import render
from rest_framework import viewsets

from .models import Hello
from .serializers import HelloSerializer
# Create your views here.


class HelloViewSet(viewsets.ModelViewSet):

    queryset = Hello.objects.all()
    serializer_class = HelloSerializer
