from django.http import HttpResponse
from django.shortcuts import render
from .models import Job


def job_listing(request):
    total_jobs = Job.objects.all()
    context = {
        'jobs': total_jobs,
        'count_jobs': Job.objects.count()
    }
    return render(request, 'job_listing.html', context)


def about(request):
    context = {
    }
    return render(request, 'about.html', context)


def service(request):
    context = {
    }
    return render(request, 'service.html', context)


