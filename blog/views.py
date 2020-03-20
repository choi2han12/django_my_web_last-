from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')


def post_detail(request, post_id):
    blog_post = Post.objects.get(pk=post_id)

    return render(
        request,
        'blog/post_detail.html',
        {
            'blog_post': blog_post,

        }
    )










#
# def index(request):
#   posts=Post.objects.all()
#
#    return render(
#        request,
#        'blog/index.html',
#    {'posts' : posts,
#     'a_plus_b': 1+3,
#
#     }
#    )