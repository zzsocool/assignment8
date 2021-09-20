from django.urls import path
from blogging.views import PostListview, PostDetailview

urlpatterns = [    
    path('', PostListview.as_view(), name="blog_index"),
    path('posts/<int:pk>/', PostDetailview.as_view(), name="blog_detail")
]


