from django.shortcuts import render
from django.contrib import messages, auth
from django.views.generic import CreateView, FormView, RedirectView, ListView, TemplateView, View
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


# def search_job(request):
#     context = {
#     }
#     print("search====================", request)
#     return


class JobListView(ListView):

    template_name = "job_listing.html"
    model = Job
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        context['count_jobs'] = Job.objects.count()
        return context


def searchjob(request):
    context = {
    }
    return render(request, 'home.html', context)


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)


