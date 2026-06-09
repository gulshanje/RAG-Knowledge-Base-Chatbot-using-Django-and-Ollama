from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Document
from .serializers import DocumentSerializer

from django.http import JsonResponse
from django.contrib.auth.models import User

def test_view(request):
    return JsonResponse({"message": "working"})

class DocumentUploadView(
    generics.CreateAPIView
):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [
        AllowAny
    ]
   
    def perform_create(self, serializer):
        user = User.objects.first()
        print(type(user))
        serializer.save(uploaded_by=user)
    
    
    