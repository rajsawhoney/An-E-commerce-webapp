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
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from product import views
from photos.views import creatememe, MemeCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    url('oauth/', include('social_django.urls', namespace='social')),

    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^product/',
        include(('product.urls', 'app_name'), namespace='product')),
    url(r'^accounts/', include(('accounts.urls', 'app_name'), namespace=('accounts'))),
    url(r'^search/', include(('search.urls', 'app_name'), namespace=('search'))),
    url(r'^cart/', include(('cart.urls', 'app_name'), namespace=('cart'))),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('creatememe/', MemeCreateView.as_view(), name='creatememe')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
