from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
# from .models import Post, Category
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist, ValidationError



# Create your views here.
class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts,
            # 'title': '글 목록',
        }
        return render(request, 'blog/post_list.html', context)


class Write(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {
            'form': form,
            # 'title': ,
        }
        return render(request, 'blog/post_form.html', context)
    
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:list')
        
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html', context)


class Detail(View):
    def get(self, request, pk):
        # post = Post.objects.get(pk=pk)
        post = Post.objects.prefetch_related('comment_set').get(pk=pk)
        comments = post.comment_set.all()
        cm_form = CommentForm()

        if post.writer != request.user:
            post.view_count = post.view_count + 1
            post.save()

        context = {
            'post_id': pk,
            'post_title': post.title,
            'post_writer': post.writer,
            'post_content': post.content,
            'post_category': post.category,
            'post_created_at': post.created_at,
            'post_image': post.image,
            'view_count': post.view_count,
            'comments': comments,
            'cm_form': cm_form,
        }
        return render(request, 'blog/post_detail.html', context)


class Update(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title': post.title, 'content': post.content, 'category': post.category, 'image': post.image})
        context = {
            'form': form,
            'post': post,
        }
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, request.FILES) # , request.FILES
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.category = form.cleaned_data['category']
            post.image = form.cleaned_data['image']
            post.save()
            return redirect('blog:detail', pk=pk)
        
        # context = {
        #     'form': form
        # }
        # return render(request, 'blog/post_edit.html', context)


class Delete(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('blog:list')
    
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return HttpResponse("<h1>존재하지 않는 게시글입니다</h1>")
        
        post.delete()
        return redirect('blog:list')
    

class Search(View):
    def get(self, request):
        category = request.GET.get('category')
        sort_by = request.GET.get('sort_by', 'created_at')

        if category:
            posts = Post.objects.filter(category=category).order_by(sort_by)
        else:
            posts = Post.objects.all().order_by(sort_by)

        context = {
            'posts': posts,
        }
        return render(request, 'blog/post_list.html', context)


class CommentWrite(LoginRequiredMixin ,View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)

        if form.is_valid():
            content = form.cleaned_data['content']
            writer = request.user

            try:
                comment = Comment.objects.create(post=post, content=content, writer=writer)
                return redirect('blog:detail', pk=pk)
            except ObjectDoesNotExist as e:
                print('Post does not exits', str(e))
            except ValidationError as e:
                print('Validation error occurred', str(e))
            return redirect('blog:detail', pk=pk)    

        context = {
            'post_id': pk,
            'comments': post.comment_set.all(),
            'cm_form': form,
        }
        return render(request, 'blog/post_detail.html', context)