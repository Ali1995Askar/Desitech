from django.views.generic import ListView
from jobs.models import Job
from accounts.models.Country import Country
from accounts.models.City import City


class AllJobsView(ListView):

    model = Job
    template_name = 'list_jobs.html'
    context_object_name = 'jobs'
  
    ordering = ['date']
    jobs = Job.job_manger.all()
    
    def get_context_data(self, **kwargs):
        context = super(AllJobsView, self).get_context_data(**kwargs)
        Countries = Country.objects.all()
        Cities = City.objects.all()
        jobs = self.get_queryset()
        
        context['jobs'] = jobs
        context['jobsCount'] = len (jobs)
        context['Countries'] = Countries
        context['Cities'] = Cities

        return context