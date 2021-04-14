from .models import PostFile, Post
from rest_framework import generics
from .serializers import PostSerializer, PostFileSerializer
import base64
from django.core.files.base import ContentFile, File
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework import status


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
    
    def create(self, request, *args, **kwargs):
        
        if len(request.data.keys()) > 1:        
            draft_request_data = []        
            
            for key, value in request.data.items():                       
                
                name_file = {
                    "name": key,
                    "file": value                
                }                                                
                draft_request_data.append(name_file)
                print(key, value)
                            
            kwargs["data"] = draft_request_data                                                        
            serializer = self.get_serializer(data=draft_request_data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            
            name_file = {
                    "name": request.data.keys()[0],
                    "file": request.data.values()[0]                
                }
            print(name_file)            
            kwargs["data"] = name_file
            serializer = self.get_serializer(data=name_file, many=False)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)            
    