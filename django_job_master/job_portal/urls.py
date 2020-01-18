from django.urls import path
from . import views
from .views import JobListView, ApplyJobView, JobDetailsView
from django.views.generic.base import TemplateView

app_name = 'job_portal'

urlpatterns = [
    path('job_listing/', JobListView.as_view(), name='job_listing'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('login', views.LoginView.as_view(), name='login'),
    path('login', TemplateView.as_view(template_name='home.html'), name='login'),
    path('search_job/', views.searchjob, name='search_job'),
    path('apply_job/', views.apply_job, name='apply_job'),
    # path('apply_job/<int:job_id>', ApplyJobView.as_view(), name='apply_job'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail')
]
