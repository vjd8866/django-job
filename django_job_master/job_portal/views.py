from django.shortcuts import render
from django.contrib import messages, auth
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView, ListView, TemplateView, View, DetailView
from .models import Job, Applicant
from .forms import ApplyJobForm


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


def apply_job(request):
    context = {}
    print("apply-----------------------", request)
    return render(request, 'apply_job_form.html', context)


def searchjob(request):
    context = {
    }
    return render(request, 'home.html', context)


class JobListView(ListView):

    template_name = "job_listing.html"
    model = Job
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        context['count_jobs'] = Job.objects.count()
        return context


class SubmitJobView(CreateView):
    model = Applicant
    form_class = ApplyJobForm
    slug_field = 'job_id'
    slug_url_kwarg = 'job_id'

    def get_context_data(self, **kwargs):
        context = super(SubmitJobView, self).get_context_data(**kwargs)
        context['instance_class'] = self.model
        return context

    def post(self, request, *args, **kwargs):
        print("")
        # form = self.get_form()
        # if form.is_valid():
        #     messages.info(self.request, 'Successfully applied for the job!')
        #     return self.form_valid(form)

    def get_success_url(self):
        return reverse_lazy('job_portal:jobs-detail', kwargs={'id': self.kwargs['job_id']})

    def form_valid(self, form):
        applicant = Applicant.objects.filter(user_id=self.request.user.id, job_id=self.kwargs['job_id'])
        if applicant:
            messages.info(self.request, 'You already applied for this job')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class JobDetailsView(DetailView):
    model = Job
    template_name = 'job_listing.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super(JobDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)


