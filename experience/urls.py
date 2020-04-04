from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='experience-home'),
    path('new/',views.newExperiencePost, name='experience-post-create')
]

# <app>/<model>_<viewtype>.html
