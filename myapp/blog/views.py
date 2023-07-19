from django.shortcuts import render, redirect
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



class DetailView(View):
    model = Post
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    context_object_name = 'post_update'
    form_class = PostForm
    success_url = reverse_lazy('blog:list')


class PostDeleteView(DeleteView):
    model = Post