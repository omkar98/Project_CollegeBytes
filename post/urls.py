from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    HackthonPostDetailView
    )
from . import views
urlpatterns = [
    path('', views.home, name='post-home'),
    path('classView/', PostListView.as_view(), name='class-name'),
    # path('jobPost/', views.jobPost, name='job-post'),
    path('jobPost/<int:pk>/', PostDetailView.as_view(), name='job-post'),
    path('hackathonPost/<int:pk>/', HackthonPostDetailView.as_view(), name='hackathon-post'),
    path('employmentPost/new/', views.newEmploymentPost, name='employ-post-create'),
    path('hackathonPost/new/', views.newHackathontPost, name='hackathon-post-create'),
]

# <app>/<model>_<viewtype>.html
