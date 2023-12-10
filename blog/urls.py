from django.urls import path
from blog.views import PostDetailView

app-name = 'blog'

urlpatterns = [
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]

