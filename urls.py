from django.urls import path
from .views import PostListViews, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListViews.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create')
]