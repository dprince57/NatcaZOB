from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('HAWC/', views.index, name='index'),
    path('HAWC/showall/', views.showall),
    path('blogpost/', views.blogpost, name="blogpost"),
    path('details/<int:blog_id>/', views.detail, name='detail')
]