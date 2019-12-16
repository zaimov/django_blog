from django.shortcuts import render

posts = [
    {
        'author': 'John Doe',
        'title': 'blog post 1',
        'content': 'First Post content',
        'date_posted': 'December 16'
    },
    {
        'author': 'Jane Doe',
        'title': 'blog post 2',
        'content': 'Second Post content goes here',
        'date_posted': 'December 16'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
