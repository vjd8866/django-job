from django.urls import path
from . import views

app_name = 'job_portal'

urlpatterns = [
    path('job_listing/', views.job_listing, name='job_listing'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
]
