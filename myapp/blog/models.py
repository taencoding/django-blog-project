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
    image = models.ImageField(blank=True) # upload_to='media/'
    view_count = models.IntegerField(default=0)

    # def is_content_more300(self):
    #     return len(self.content) > 300
    
    # def get_content_under(self):
    #     return self.content[:300]


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    

class Recomment(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content