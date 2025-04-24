from django.urls import path
from . import views

app_name='app2'

urlpatterns = [
    # Domain urls
    path('job_list/', views.job_list, name='job_list'),
    path('add/', views.add_job, name='add_job'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_id>/apply/', views.job_application, name='job_application'),
    path('job/<int:job_id>/submit/', views.job_application, name='submit_application'),
    path('applied-jobs/', views.applied_jobs, name='applied_jobs'),
    
    # Remote urls
    path('remote_job_list/', views.remote_job_list, name='remote_job_list'),
    path('add_remote/', views.add_remote_job, name='add_remote_job'),
    path('remote_job/<int:job_id>/', views.remote_job_detail, name='remote_job_detail'),
    path('remote_job/<int:job_id>/apply/', views.remote_job_application, name='remote_job_application'),
    path('remote_job/<int:job_id>/submit/', views.remote_job_application, name='submit_remote_application'),
    path('applied-remote-jobs/', views.applied_remote_jobs, name='applied_remote_jobs'),

    # Walk-In urls
    path('walkIn_job_list/', views.walkIn_job_list, name='walkIn_job_list'),
    path('add_walkin/', views.add_walkin_job, name='add_walkin_job'),
    path('walkIn_job/<int:job_id>/', views.walkIn_job_detail, name='walkIn_job_detail'),
    path('walkIn_job/<int:job_id>/apply/', views.walkIn_job_application, name='walkIn_job_application'),
    path('walkIn_job/<int:job_id>/submit/', views.walkIn_job_application, name='submit_walkin_application'),
    path('applied-walkin-jobs/', views.applied_walkin_jobs, name='applied_walkin_jobs'),
]