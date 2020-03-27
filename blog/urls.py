from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
]

# <app>/<model>_<viewtype>.html
