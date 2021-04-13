from .models import PostFile, Post
from rest_framework import generics
from .serializers import PostSerializer, PostFileSerializer
import base64
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, JSONParser

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, JSONParser]    
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
    

class FileList(generics.ListCreateAPIView):
    queryset = PostFile.objects.all()
    serializer_class = PostFileSerializer    
    