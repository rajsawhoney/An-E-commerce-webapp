"""my_e_commerce_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
from questions_ans.views import post_ques_ans
from reviews.views import post_review


urlpatterns = [
    url(r'list/', views.HomeView.as_view(), name='product_list'),
    url(r'^categorical/(?P<slug>[\w-]+)/',
        views.CategoryView.as_view(), name='category_view'),
    url(r'^categorylist/',
        views.CategoryListView.as_view(), name='category_list_view'),
    # url(r'^test', views.TestIndex, name='test'),
    url(r"^detail/(?P<pk>[\w-]+)/",
        views.ProductDetailView, name="detail_view"),
    url(r'^new_product/', views.ProductCreateView.as_view(), name='create_product'),
    url(r'^ques_ans/(?P<slug>[\w-]+)/', post_ques_ans, name='ques-ans'),
    url(r'^review/(?P<slug>[\w-]+)/', post_review, name='review'),

]
