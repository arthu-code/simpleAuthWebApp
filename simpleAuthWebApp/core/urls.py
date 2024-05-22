from django.urls import path
from django.views.generic.base import TemplateView
from . import views


urlpatterns =[
    # path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('signup/', views.signup, name='signup'),
]