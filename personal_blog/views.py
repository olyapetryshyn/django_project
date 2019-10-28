from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Corey',
        'title': 'Blogpost1',
        'content': 'bfjvbdjkv',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Olya',
        'title': 'Blogpost2',
        'content': 'bfjvbdjkvdfbdmbe',
        'date_posted': 'August 28, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
