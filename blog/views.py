from .models import Post, PostFile
from rest_framework import generics
from .serializers import PostSerializer, PostFileSerializer
import base64
from django.core.files.base import ContentFile


def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))

class PostList(generics.ListCreateAPIView):
    queryset = PostFile.objects.all()
    serializer_class = PostFileSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class FileList(generics.ListCreateAPIView):
    queryset = PostFile.objects.all()
    serializer_class = PostFileSerializer
    