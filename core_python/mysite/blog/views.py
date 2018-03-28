from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
# from django.template import RequestContext
from blog.models import BlogPost

# Create your views here.
def archive(request):
    posts = BlogPost.objects.all().order_by('-timestamp')[:10]
    return render(request, "archive.html",
    {'posts': posts, }
    )

def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(
        title=request.POST.get('title'),
        body=request.POST.get('body'),
        timestamp=datetime.now(),
        ).save()
    return HttpResponseRedirect('/blog/')
