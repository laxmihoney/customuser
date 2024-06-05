from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name = 'home'),
    path('login/', views.login_view, name = 'login'),
    path('products/', views.products, name = 'products'),
    path('services/', views.services, name = 'serives'),
    path('signup/', views.signup_view, name = 'signup'),
    path('profile/', views.profile, name = 'profile'),
    path('logout/', views.logout_view, name = 'logout'),
    path('about/', views.about,name="about"),
    path('verify/', views.verify,name='verify'),
    path('verify/verifycode/', views.verifycode,name="verifycode")
]