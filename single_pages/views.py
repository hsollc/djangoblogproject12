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
import time
from newsapi import NewsApiClient
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

def news(request):
    r = requests.get(
        'https://newsapi.org/v2/top-headlines?country=us&apiKey=c66416a0443445a896fe5e0eff1b1bc5')
    data = json.loads(r.content)
    headlines= data['articles']

    newslines =[]

    for i in range(len(headlines)):
        if i < 10:
            newslines.append(headlines[i]['title'])

    return render(request, 'single_pages/news.html', context={"newslines": newslines})

from django.shortcuts import render
from newsapi import NewsApiClient
from datetime import datetime, timedelta

def cultureNews(request):
    newsapi = NewsApiClient(api_key="c66416a0443445a896fe5e0eff1b1bc5")
    # topheadlines = newsapi.get_top_headlines(sources='bbc-news')
    now = datetime.now()
    before_one_day =  now - timedelta(days=25)

    all_articles = newsapi.get_everything(q='art',
                                          # sources='bbc-news,the-verge',
                                          # domains='bbc.co.uk,techcrunch.com',
                                          from_param=before_one_day,
                                          to=now,
                                          language='en',
                                          sort_by='relevancy',
                                          # page=1
                                          )

    # articles = topheadlines['articles']
    articles = all_articles['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        if i < 10:
            myarticles = articles[i]

            news.append(myarticles['title'])
            desc.append(myarticles['description'])
            img.append(myarticles['urlToImage'])
            url.append(myarticles['url'])

    mylist = zip(news, desc, img, url)


    return render(request, 'single_pages/cultureNews.html', context={"mylist":mylist})

# import requests
# import json

# def newsInfo(request):
#     r = requests.get(
#         'https://api.mediastack.com/v1/news?acess_key=dcdde6a475321e873ad958c16c52a68b&countries=us')
#     data = json.loads(r.content)
#
#     articles = data['articles']
#     # res = r.jason()
#     # data = res['data']
#
#     head = []
#     description = []
#     image = []
#     url = []
#
#
#     for i in range(len(articles)):
#         myarticles = articles[i]
#
#         head.append(myarticles['title'])
#         description.append(myarticles['description'])
#         image.append(myarticles['image'])
#         url.append(myarticles['url'])
#
#     news = zip(head, description, image, url)
#
#     context = {
#         "news": news
#     }
#     return render(request, 'single_pages/cultureNews.html', context)


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

def coding(request):
    return render(
        request,
        'single_pages/coding.html'
    )