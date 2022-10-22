from typing import Dict, Any

from django.shortcuts import render
from blog.models import Post


def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:5]

    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
        }
    )


def hsollc(request):
    return render(
        request,
        'single_pages/hsollc.html'
    )

import requests
import json
import os

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "True"

def art(request):
    return render(
        request,
        'single_pages/art.html'
    )

def golf(request):
    return render(
        request,
        'single_pages/golf.html'
    )

