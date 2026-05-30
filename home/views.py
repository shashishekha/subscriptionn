from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer, BlogDetailSerializer
from . import mixins


class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer

    def list(self, request, *args, **kwargs):
        return Response({
            'status':'True',
            'message':'blogs fetched',
            'data':{
            'count': self.queryset.count(), 
            'blogs':BlogSerializer(self.queryset, many = True).data
            }
        })
    


