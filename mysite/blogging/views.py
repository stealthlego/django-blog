from django import template
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args:\n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")


class BlogListView(ListView):
    model = Post

    queryset = Post.objects.order_by("-published_date")
    queryset = queryset.exclude(published_date=None)
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):
    model = Post
    # template_name = 'blogging/detail.html'
    def get(self, request, *args, **kwargs):
        published = Post.objects.exclude(published_date__exact=None)
        try:
            post = published.get(pk=self.get_object().id)
        except Post.DoesNotExist:
            raise Http404
        context = {"object": post}
        return render(request, "blogging/detail.html", context)


# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     template = loader.get_template('blogging/list.html')
#     context = {'posts': posts}
#     return render(request, 'blogging/list.html', context)

# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)
#
