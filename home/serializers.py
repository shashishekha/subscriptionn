from rest_framework import serializers
from . import models


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = ['blog_title','uid']



class BlogDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        exclude = ['updated_at',]