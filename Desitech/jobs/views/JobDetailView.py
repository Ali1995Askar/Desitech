from django.views.generic.detail import DetailView
from jobs.models import Job
from django.contrib.auth.decorators import login_required




class JobDetailView(DetailView):

    model = Job
    template_name = 'job_detail.html'
    context_object_name = 'job'
