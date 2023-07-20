from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
User = get_user_model()


# class Category(models.Model):
#     name = models.CharField(max_length=50, help_text="카테고리를 작성하세요.")

#     def __str__(self):
#         return self.name


class Post(models.Model):
    title = models.CharField(verbose_name='글 제목', max_length=30)
    content = models.TextField(verbose_name='글 내용')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, verbose_name="카테고리")

    # def is_content_more300(self):
    #     return len(self.content) > 300
    
    # def get_content_under(self):
    #     return self.content[:300]