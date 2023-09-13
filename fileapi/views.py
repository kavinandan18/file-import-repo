# views.py
from rest_framework import viewsets,status
from .models import MonetaryPenalty, FileMetadata
from .serializer import MonetaryPenaltySerializer, FileMetadataSerializer
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

class MonetaryPenaltyListView(generics.ListCreateAPIView):
    queryset = MonetaryPenalty.objects.all()
    serializer_class = MonetaryPenaltySerializer

class MonetaryPenaltyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonetaryPenalty.objects.all()
    serializer_class = MonetaryPenaltySerializer


class GetFileMetadataByIdView(generics.RetrieveAPIView):
    queryset = FileMetadata.objects.all()
    serializer_class = FileMetadataSerializer
    lookup_field = 'file_id'  # Specify the lookup field as 'file_id'

class GetAllFileMetadataView(generics.ListAPIView):
    queryset = FileMetadata.objects.all()
    serializer_class = FileMetadataSerializer
