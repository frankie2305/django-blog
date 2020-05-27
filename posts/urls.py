from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(extra_context={ 'title': 'Post detail' }), name='detail'),
    path('create/', PostCreateView.as_view(extra_context={ 'title': 'New post', 'legend': 'New post', 'submit': 'Create' }), name='create'),
    path('<int:pk>/update', PostUpdateView.as_view(extra_context={ 'title': 'Update post', 'legend': 'Update post', 'submit': 'Update' }), name='update'),
    path('<int:pk>/delete', PostDeleteView.as_view(extra_context={ 'title': 'Delete post', 'legend': 'Delete post' }), name='delete'),
    path('<str:username>/', UserPostListView.as_view(), name='user-posts'),
]
