from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})

def react(request):
    return render(request, 'mysite/html/build/index.html', {})
