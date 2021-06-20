from django.urls import path
from . import views
from nhaphang import views as view_nhaphang
from core.views import HomeView
app_name ='account'
urlpatterns = [
   
    path('home',HomeView.as_view(),name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),   
]