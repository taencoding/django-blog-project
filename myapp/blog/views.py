from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

# Create your views here.
class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts,
            # 'title': '글 목록',
        }
        return render(request, 'blog/post_list.html', context)


class Write(View):
    def get(self, request):
        form = PostForm()
        context = {
            'form': form,
            # 'title': ,
        }
        return render(request, 'blog/post_form.html', context)
    
    def post(self, request):
        form = PostForm(request.POST)

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
        post = Post.objects.get(pk=pk)

        context = {
            'post_id': pk,
            'post_title': post.title,
            'post_writer': post.writer,
            'post_content': post.content,
            'post_created_at': post.created_at,
        }
        return render(request, 'blog/post_detail.html', context)


class Update(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title': post.title, 'content': post.content})
        context = {
            'form': form,
            'post': post,
        }
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST)

        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)
        
        # context = {
        #     'form': form
        # }
        # return render(request, 'blog/post_edit.html', context)


class Delete(DeleteView):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')