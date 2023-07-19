from django.urls import path
from blog.views import PostList, Write, DetailView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('write/', Write.as_view(), name='write'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
]
