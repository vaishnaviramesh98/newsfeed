from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),
    path("home",views.home,name="home"),
    path("newsfeed", views.newsfeed,name="newsfeed"),
    path("view_feeds", views.view_feeds, name="view_feeds"),
    path("view_users", views.view_users, name="view_users")
    ]