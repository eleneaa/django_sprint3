from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Blog_Category


def index(request):
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]

    context = {
        'post_list': post_list
    }
    return render(request, "blog/index.html", context)


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id, is_published=True)

    if post.pub_date > timezone.now() or not post.category.is_published:
        raise Http404("Публикация недоступна.")

    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Blog_Category,
                                 slug=category_slug,
                                 is_published=True)

    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    )

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
