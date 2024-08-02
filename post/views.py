from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from post.serilazers import PostSerialazer
from post.models import News


# Create your views here.

# class PostListAPI(ListAPIView):
#     serializer_class = PostSerialazer
#     queryset = News.objects.all()
# class PostCreateAPI(CreateAPIView):
#     serializer_class = PostSerialazer
#     queryset = News.objects.all()
class PostListAPI(ListCreateAPIView):
    serializer_class = PostSerialazer
    queryset = News.objects.all()


class PostDetailAPI(RetrieveAPIView):
    serializer_class = PostSerialazer
    queryset = News.objects.all()


class PutPostAPI(UpdateAPIView):
    serializer_class = PostSerialazer
    queryset = News.objects.all()


class DELETEPostAPI(DestroyAPIView):
    serializer_class = PostSerialazer
    queryset = News.objects.all()
