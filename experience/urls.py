from django.urls import path
from .views import  ExperienceListView
from . import views

urlpatterns = [
    path('', views.home, name='experience-home'),
    path('new/',views.newExperiencePost, name='experience-post-create'),
    path('company/<int:organization>/', ExperienceListView.as_view(), name='company-experiences'),
]

# <app>/<model>_<viewtype>.html
