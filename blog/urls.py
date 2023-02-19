from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='home_page'),
    path('posts/', PostView.as_view(), name='post_page'),
    path('posts/<slug:slug>', SinglePostView.as_view(), name='post_detail_page'),
]
