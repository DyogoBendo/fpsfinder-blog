from .models import PostFile, Post
from rest_framework import generics
from .serializers import PostSerializer, PostFileSerializer
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

class SetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 20
               

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, JSONParser]    
    pagination_class = SetPagination
    
    def list(self, request, *args, **kwargs):
        
        has_page = True if request.GET.get("page") else False                
        if has_page:                                                               
            queryset = self.filter_queryset(Post.objects.filter(published__exact=False, featured__exact=False).order_by("-last_edited_at")[3:])
            page = self.paginate_queryset(queryset)                                                    
                
            if page is not None:
                serializer = self.get_serializer(page, many=True, context={"request":request})                            
                return self.get_paginated_response(serializer.data)                        
            
            serializer = self.get_serializer(queryset, many=True)        
            return Response({
                serializer.data
            })
        else:
            try:
                queryset = self.filter_queryset(Post.objects.all().order_by("-last_edited_at"))
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        

            
        

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
        

class FileList(generics.ListCreateAPIView):    
    queryset = PostFile.objects.all()
    serializer_class = PostFileSerializer    
    
    def create(self, request, *args, **kwargs):
        many = len(request.data.keys()) > 1                        
        draft_request_data = []        
        
        for key, value in request.data.items():                                   
            name_file = {
                "name": key,
                "file": value                
            }                                                
            draft_request_data.append(name_file)                
                        
        kwargs["data"] = data = draft_request_data if many else name_file                                    
        serializer = self.get_serializer(data=data, many=many)                                                                                                    
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        headers["Access-Control-Allow-Origin"] = "*"
        headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        headers["Access-Control-Max-Age"] = "1000"
        headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"        
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class FeaturedDetail(APIView):    
    def put(self, request, pk):
        
        try:
            model_old = get_object_or_404(Post, featured=True)                                
            data_old = {"featured": False}         
            serializer = PostSerializer(model_old, data=data_old, partial=True)
            
            if serializer.is_valid():
                serializer.save()
        except:
            pass
        model_1 = get_object_or_404(Post, pk=pk)                    
        data = {"featured": True}
        serializer = PostSerializer(model_1, data=data, partial=True)                
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        try: 
            model = get_object_or_404(Post, featured=True)                                                 
            serializer = PostSerializer(model, partial=True)            
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LatestPostList(APIView):
    def get(self, request):
        try: 
            post = Post.objects.filter(published__exact=True, featured__exact=False).order_by('-last_edited_at')[:3]
            print(post)
            serializer = PostSerializer(post, many=True)
            return Response(serializer.data)
        except:
            print("banana")
            return Response(status=status.HTTP_400_BAD_REQUEST)
