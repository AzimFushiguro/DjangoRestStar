from django.urls import path
from post.views import PostListAPI, PostDetailAPI,PutPostAPI,DELETEPostAPI,ArticleListAPI,ArticlePutAPI,ArticleDELETEApi,ArticleDeatailAPI,BlogListAPI,BlogPutAPI,BlogDELETEApi,BlogDeatailAPI,ProductPutAPI,ProductDELETEApi,ProductListAPI,ProductDeatailAPI,CarDELETEApi,CarDeatailAPI,CarListAPI,CarPutAPI,ApplicationDeatailAPI,ApplicationPutAPI,ApplicationListAPI,ApplicationDELETEApi,CommentaryDELETEApi,CommentaryListAPI,CommentaryDeatailAPI,CommentaryPutAPI

urlpatterns = [
    path("api/posts/", PostListAPI.as_view(), name="post_list"),
    path("api/posts/<int:pk>/", PostDetailAPI.as_view(), name="post_detail"),
    path("api/posts/<int:pk>/update/", PutPostAPI.as_view(), name="put_detail"),
    path("api/posts/<int:pk>/delete/", DELETEPostAPI.as_view(), name="delete"),

    path("api/article/", ArticleListAPI.as_view()),
    path("api/article/<int:pk>/update", ArticlePutAPI.as_view()),
    path("api/article/<int:pk>/", ArticleDeatailAPI.as_view()),
    path("api/article/<int:pk>/delete", ArticleDELETEApi.as_view()),

    path("api/blog/", BlogListAPI.as_view()),
    path("api/blog/<int:pk>/update", BlogPutAPI.as_view()),
    path("api/blog/<int:pk>/", BlogDeatailAPI.as_view()),
    path("api/blog/<int:pk>/delete", BlogDELETEApi.as_view()),

    path("api/product/", ProductListAPI.as_view()),
    path("api/product/<int:pk>/update", ProductPutAPI.as_view()),
    path("api/product/<int:pk>/", ProductDeatailAPI.as_view()),
    path("api/product/<int:pk>/delete", ProductDELETEApi.as_view()),

    path("api/car/", CarListAPI.as_view()),
    path("api/car/<int:pk>/update", CarPutAPI.as_view()),
    path("api/car/<int:pk>/", CarDeatailAPI.as_view()),
    path("api/cara/<int:pk>/delete", CarDELETEApi.as_view()),

    path("api/application/", ApplicationListAPI.as_view()),
    path("api/application/<int:pk>/update", ApplicationPutAPI.as_view()),
    path("api/application/<int:pk>/", ApplicationDeatailAPI.as_view()),
    path("api/application/<int:pk>/delete", ApplicationDELETEApi.as_view()),

    path("api/comment/", CommentaryListAPI.as_view()),
    path("api/comment/<int:pk>/update", CommentaryPutAPI.as_view()),
    path("api/comment/<int:pk>/", CommentaryDeatailAPI.as_view()),
    path("api/comment/<int:pk>/delete", CommentaryDELETEApi.as_view()),
    # path("api/posts/create/", PostCreateAPI.as_view(), name="post_create"),
]
