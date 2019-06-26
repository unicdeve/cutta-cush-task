from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin


urlpatterns = [
  path('', include('camelapp.urls')),
  path('admin/', admin.site.urls)
]
