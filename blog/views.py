from django.shortcuts import render
from .models import Category
from .models import Post
from . import urls
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['uncategorized_posts'] = Post.objects.filter(category=None).count()

        return context



class PostDetail(ListView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['uncategorized_posts'] = Post.objects.filter(category=None).count()

        return context






# class PostDetail(DetailView):
#
#     model = Post
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(PostDetail, self).get_context_data(**kwargs)
#         context['category_list'] = Category.objects.all()
#         context['uncategorized_posts'] = Post.objects.filter(category=None).count()
#
#         return context
































# class PostDetail(DetailView):
#     model = Post
#     #
    # def post_detail(request, pk):
    #     post = get_object_or_404(Post, pk=pk)
    #     return render(request, 'blog/post_detail.html', {'post': post})
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(PostDetail, self).get_context_data(**kwargs)
    #     context['category_list'] = Category.objects.all()
    #     context['uncategorized_posts'] = Post.objects.filter(category=None).count()
    #
    #     return context




























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