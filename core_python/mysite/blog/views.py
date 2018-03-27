from django.shortcuts import render
from datetime import datetime
from blog.models import BlogPost

# Create your views here.
def archive(request):
    post = BlogPost(title='mocktitle', body='mockbody', timestamp=datetime.now())
    return render(request, 'archive.html', {'posts': [post]})
