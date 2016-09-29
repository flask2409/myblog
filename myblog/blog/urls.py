from django.conf.urls import include, url
from .views import listpost, detailpost, category

urlpatterns = [

    url(r'^$', listpost, name="post_list"),
    url(r'^post/(?P<id>[0-9]+)$', detailpost, name="post_detail"),
    url(r'^category/(?P<id>[0-9]+)$', category, name = 'category_list'),
]