from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'),

    path('api', views.list2, name='list2'),
    # ex: /polls/5/
    path('api/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('api/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('api/<int:question_id>/vote/', views.vote, name='vote'),
    
]

from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]