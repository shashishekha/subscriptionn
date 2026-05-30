
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Blog

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