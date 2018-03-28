from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader, Context
from blog.models import BlogPost

# Create your views here.
def archive(request):
    posts = BlogPost.objects.all().order_by('-timestamp')[:10]
    return render(request, "archive.html",
    {'posts': posts, }
    )
