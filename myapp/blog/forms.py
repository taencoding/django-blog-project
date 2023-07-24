from django import forms
from .models import Post, Comment, ReComment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']


class ReCommentFrom(forms.ModelForm):

    class Meta:
        model = ReComment
        fields = ['content']