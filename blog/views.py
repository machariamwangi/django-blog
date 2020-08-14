from django.shortcuts import render
# from django.http import HttpResponse
posts = [
    {
        'author': 'elijah',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'AUGUST 14 2020',
    },
    {
        'author': 'jOHN DOE',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'AUGUST 15 2020',
    }

]

# Create your views here.


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
