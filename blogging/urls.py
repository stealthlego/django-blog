from django.urls import path
from blogging.views import BlogListView, BlogDetailView, BlogFeed

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    # path('', stub_view, name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path('feed/', BlogFeed(), name='blog_feed'),
]
