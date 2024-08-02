from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from post.serilazers import PostSerialazer,ArticleSerialazer,BlogSerialazer,ProductSerialazer,CarSerialazer,ApplicationSerialazer,CommentSerialazer
from post.models import News,Article,Blog,Product,Car,Application,Comment


# Create your views here.

# class PostListAPI(ListAPIView):
#     serializer_class = PostSerialazer
#     queryset = News.objects.all()
# class PostCreateAPI(CreateAPIView):
#     serializer_class = PostSerialazer
#     queryset = News.objects.all()
#GET+POST
class PostListAPI(ListCreateAPIView):
    serializer_class = PostSerialazer
    queryset = News.objects.all()

#GET BY ID
class PostDetailAPI(RetrieveAPIView):
    serializer_class = PostSerialazer
    queryset = News.objects.all()

#Put update
class PutPostAPI(UpdateAPIView):
    serializer_class = PostSerialazer
    queryset = News.objects.all()
#DELETE
class DELETEPostAPI(DestroyAPIView):
    serializer_class = PostSerialazer
    queryset = News.objects.all()

#Article
class ArticleListAPI(ListCreateAPIView):
    serializer_class = ArticleSerialazer
    queryset = Article.objects.all()
class ArticleDeatailAPI(RetrieveAPIView):
    serializer_class = ArticleSerialazer
    queryset = Article.objects.all()

class ArticlePutAPI(UpdateAPIView):
    serializer_class = ArticleSerialazer
    queryset = Article.objects.all()

class ArticleDELETEApi(DestroyAPIView):
    serializer_class = ArticleSerialazer
    queryset = Article.objects.all()

#Blog
class BlogListAPI(ListCreateAPIView):
    serializer_class = BlogSerialazer
    queryset = Blog.objects.all()
class BlogDeatailAPI(RetrieveAPIView):
    serializer_class = BlogSerialazer
    queryset = Blog.objects.all()

class BlogPutAPI(UpdateAPIView):
    serializer_class = BlogSerialazer
    queryset = Blog.objects.all()

class BlogDELETEApi(DestroyAPIView):
    serializer_class = BlogSerialazer
    queryset = Blog.objects.all()


class ProductListAPI(ListCreateAPIView):
    serializer_class = ProductSerialazer
    queryset = Product.objects.all()
class ProductDeatailAPI(RetrieveAPIView):
    serializer_class = ProductSerialazer
    queryset = Product.objects.all()

class ProductPutAPI(UpdateAPIView):
    serializer_class = ProductSerialazer
    queryset = Product.objects.all()

class ProductDELETEApi(DestroyAPIView):
    serializer_class = ProductSerialazer
    queryset = Product.objects.all()


class CarListAPI(ListCreateAPIView):
    serializer_class = CarSerialazer
    queryset = Car.objects.all()
class CarDeatailAPI(RetrieveAPIView):
    serializer_class = CarSerialazer
    queryset = Car.objects.all()

class CarPutAPI(UpdateAPIView):
    serializer_class = CarSerialazer
    queryset = Car.objects.all()

class CarDELETEApi(DestroyAPIView):
    serializer_class = CarSerialazer
    queryset = Car.objects.all()


class ApplicationListAPI(ListCreateAPIView):
    serializer_class = ApplicationSerialazer
    queryset = Application.objects.all()
class ApplicationDeatailAPI(RetrieveAPIView):
    serializer_class = ApplicationSerialazer
    queryset = Application.objects.all()

class ApplicationPutAPI(UpdateAPIView):
    serializer_class = ApplicationSerialazer
    queryset = Application.objects.all()

class ApplicationDELETEApi(DestroyAPIView):
    serializer_class = ApplicationSerialazer
    queryset = Application.objects.all()


class CommentaryListAPI(ListCreateAPIView):
    serializer_class = CommentSerialazer
    queryset = Comment.objects.all()
class CommentaryDeatailAPI(RetrieveAPIView):
    serializer_class = CommentSerialazer
    queryset = Comment.objects.all()

class CommentaryPutAPI(UpdateAPIView):
    serializer_class = CommentSerialazer
    queryset = Comment.objects.all()

class CommentaryDELETEApi(DestroyAPIView):
    serializer_class = CommentSerialazer
    queryset = Comment.objects.all()
