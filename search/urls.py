from django.conf.urls import url
from django.urls import path
from .views import SearchResultView, ajax_search

urlpatterns = [
    url(r'^$', SearchResultView.as_view(), name='result_list'),
    path('product/', ajax_search, name='search-product')
]
