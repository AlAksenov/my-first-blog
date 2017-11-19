from django.conf.urls import url

from . import views

app_name = 'default_app'
urlpatterns = [
    # ex: /polls/
    url(r'^login/', views.login_view, name='login'),
]