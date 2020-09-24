from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('radar', views.RadarView.as_view(), name='radar'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('regist', views.Regist.as_view(), name='regist'),
    path('getUser', views.GetUsersView.as_view(), name='getUser')
]