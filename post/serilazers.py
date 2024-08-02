from rest_framework import serializers
from post.models import News, Car, Comment, Product, Article, Application, Blog


class PostSerialazer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "description", "body")


class ArticleSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "description", "body", "article_type", "publisher_year")


class BlogSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", "title", "description", "author_name", "publisher_year")


class ProductSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "qty", "price", "brand_name")


class CarSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "brand", "name", "power", "color", "country", "year")


class ApplicationSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ("id", "first_name", "last_name", "middle_name", "birth_date", "birth_country", "comment")


class CommentSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "name", "is_confirmed")
