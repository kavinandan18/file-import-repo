from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MonetaryPenaltyListView, MonetaryPenaltyDetailView, GetFileMetadataByIdView, GetAllFileMetadataView


urlpatterns = [
    path('file-metadata/get-file-by-id/<str:file_id>/', GetFileMetadataByIdView.as_view(), name='get_file_by_id'),
    path('file-metadata/get-all-file-metadata/', GetAllFileMetadataView.as_view(), name='get_all_file_metadata'),
    path('monetary-penalties/', MonetaryPenaltyListView.as_view(), name='monetary_penalty_list'),
    path('monetary-penalties/<int:pk>/', MonetaryPenaltyDetailView.as_view(), name='monetary_penalty_detail'),
]
