from django.shortcuts import render
from .models import Post

posts = [
    {
        "author": "Destiny Frank",
        "title": "Blog post 1",
        "content": "This is my first blog post",
        "date_posted": "5th December, 2022",
    },
    {
        "author": "Senpo",
        "title": "Blog post 2",
        "content": "This is my second blog post",
        "date_posted": "14th December, 2022",
    },
]


def home_page(request):
    context = {"posts": Post.objects.all()}

    return render(request, template_name="blog/home.html", context=context)


def about_page(request):
    return render(
        request, template_name="blog/about.html", context={"title": "About Page"}
    )
