from django.urls import path
from post.views import PostListAPI, PostDetailAPI,PutPostAPI,DELETEPostAPI

urlpatterns = [
    path("api/posts/", PostListAPI.as_view(), name="post_list"),
    path("api/posts/<int:pk>/", PostDetailAPI.as_view(), name="post_detail"),
    path("api/posts/<int:pk>/update/", PutPostAPI.as_view(), name="put_detail"),
    path("api/posts/<int:pk>/delete/", DELETEPostAPI.as_view(), name="delete")
    # path("api/posts/create/", PostCreateAPI.as_view(), name="post_create"),
]
