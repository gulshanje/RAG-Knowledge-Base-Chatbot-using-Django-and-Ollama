from django.urls import path
from .views import DocumentUploadView, test_view

urlpatterns = [
    path(
        "upload/",
        DocumentUploadView.as_view(),
        name="document-upload"
    ),
     path("test/", test_view),
]