
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls.static import static

from cafe_fanus import settings
from mainApp.views import getCategories, getProducts

urlpatterns = [
    url(r'^getCategories/$', getCategories.as_view()),
    url(r'^getProducts/$', getProducts.as_view()),
    # url(r'^getSubCategories/$', getSubCategories.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
