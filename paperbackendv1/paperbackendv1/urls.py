from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from catone import views
from django.conf.urls import url
from django.urls import include
from cattwo import viewscattwo
from fat import viewsfat


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^catone/', views.catone.as_view()),
    url(r'^cattwo/',viewscattwo.cattwo.as_view()),
    url(r'^fat/',viewsfat.fat.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)