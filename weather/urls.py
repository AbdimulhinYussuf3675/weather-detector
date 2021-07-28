from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'delete/<city_name>/', views.delete_city, name='delete_city'),
]
