from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader, Context
from blog.models import BlogPost

# Create your views here.
def archive(request):
    posts = BlogPost.objects.all()
    return render(request, "archive.html",
    {'posts': posts, }
    )
