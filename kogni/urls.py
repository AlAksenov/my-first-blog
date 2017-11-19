from django.conf.urls import url

from . import views

app_name = 'kogni'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.home, name='home'),
    url(r'^karti/(?P<karti_id>[0-9]+)$', views.karti_detail, name='detail'),
    url(r'^scenariy/7', views.my_view, name='test'),
    url(r'^scenariy/a', views.my_react11, name='test1'),
    url(r'^scenariy/b', views.my_react12, name='test2'),
    url(r'^ska', views.ska, name='ska'),
    url(r'^gorin', views.gorin, name='gorin'),
    url(r'^int', views.my_int, name='int'),


    ]
