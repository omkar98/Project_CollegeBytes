from django.urls import path
from .views import (
    PostListView,
    PostDetailView
    )
from . import views
urlpatterns = [
    path('', views.home, name='post-home'),
    path('classView/', PostListView.as_view(), name='class-name'),
    # path('jobPost/', views.jobPost, name='job-post'),
    path('jobPost/<int:pk>/', PostDetailView.as_view(), name='job-post'),
    path('employmentPost/new/', views.newEmploymentPost, name='employ-post-create'),

]

# <app>/<model>_<viewtype>.html
