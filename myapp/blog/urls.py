from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.PostList.as_view(), name='list'),
    path("write/", views.Write.as_view(), name='write'),
    path("detail/<int:pk>/", views.Detail.as_view(), name='detail'),
    path("edit/<int:pk>/", views.Update.as_view(), name='edit'),
    path("delete/<int:pk>/", views.Delete.as_view(), name='delete'),
    path("search/", views.Search.as_view(), name='search'),
    path("detail/<int:pk>/cm-write/", views.CommentWrite.as_view(), name='cm-write'),
    path("detail/<int:pk>/cm-delete/", views.CommentDelete.as_view(), name='cm-delete'),
    path("detail/<int:pk>/rcm-write/", views.ReCommentWrite.as_view(), name='rcm-write'),
    path("detail/<int:pk>/rcm-delete/", views.ReCommentDelete.as_view(), name='rcm-delete'),
]
