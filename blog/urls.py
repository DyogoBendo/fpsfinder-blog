from django.urls import path
from .views import PostList, PostDetail, FileList, FeaturedDetail, LatestPostList, PostSlugDetail

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('files/',  FileList.as_view()),
    path('featured/', FeaturedDetail.as_view()),
    path('featured/<int:pk>', FeaturedDetail.as_view()),    
    path('latest-posts/', LatestPostList.as_view()),    
    path("<slug:slug>/", PostSlugDetail.as_view({'get': 'retrieve'})),        
]