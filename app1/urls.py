from django.urls import path
from . import views

app_name='app1'

urlpatterns = [
    path('',views.landingPage,name='landingPage'),
    path('home/',views.homePage,name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/', views.register_view, name='register'),
    path('createYourOwnResume/',views.create_your_own_resume,name='create_your_own_resume'),
    path('about/',views.about_view,name='about')
    # Add other URL patterns as needed
]






