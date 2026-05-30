
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Blog
from .permissions import *
from rest_framework.authentication import TokenAuthentication

class BlogMixin:
    @action(detail=True, methods=['get'])
    def blog_detail(self, request, pk):
        try:
            blog_obj = Blog.objects.get(pk = pk)
            return Response({
                'status': True,
                'message': 'blog fetch',
                'data': self.serializer_class(blog_obj).data
            })
        except Exception as e :
            return Response({
                'status': False,
                'message': 'invalid uid',
                'data' : {}
            })
        
    @action(detail=True, methods=['patch'], permission_classes = [IsOwner], authentication_classes = [TokenAuthentication])
    def blog_update(self, request, pk):
        try:
            blog_obj = (self.get_object())

            data = request.data 

            serializer = self.serializer_class(blog_obj, data= data, partial=True)

            if serializer.is_valid():
                serializer.save()

                return Response({
                    'status': True,
                    'message': 'blog update',
                    'data': serializer.data
                })
            return Response({
                'status': True,
                'message': 'blogs not update',
                'data': serializer.errors
                })
        
        except Exception as e :
            return Response({
                'status': False,
                'message': 'Authentication Failed',
                'data' : {}
            })