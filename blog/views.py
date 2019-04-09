from django.shortcuts import render

posts = [
    {
        'author': 'Gary Waller',
        'title': 'Initial post',
        'content': 'First!!!',
        'date_posted': 'January 1, 2019'
    },
    {
        'author': 'Yael',
        'title': 'Second post',
        'content': 'Hello Dad',
        'date_posted': 'March 30, 2019'
    },

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'} )
  