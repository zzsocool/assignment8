from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic import ListView, DetailView


class PostListview(ListView):
    model = Post
    template_name = 'blogging/list.html'
    queryset = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')
    # queryset = Post.objects.order_by('-published_date')


class PostDetailview(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        context = {'object': post}
        return render(request, 'blogging/detail.html', context)

# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     context = {'posts': posts}
#     return render(request, 'blogging/list.html', context)
#
# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)
# # Create your views here.
