from django.urls import path 
from jobs.views import (JobCreateView , JobDeleteView , JobDetailView , 
                        JobUpdateView , AllJobsView  , MyJobs ,views)

from jobs.api.views.JobListView import AllJobsList
from jobs.api.views.JobByIdView import JobById

app_name = 'jobs'

urlpatterns = [
 
    path('listjobs/', AllJobsView.AllJobsView.as_view(), name='all-jobs-list'),
    path('myjobs/', MyJobs.MyJobs.as_view(),name='my-jobs'),
    path('create/', JobCreateView.JobCreateView.as_view(), name='job-create'),
    path('<int:pk>/update/',JobUpdateView.JobUpdateView.as_view(),name='job-update'),
    path('<int:pk>/delete/', JobDeleteView.JobDeleteView.as_view(),name='job-delete'),
    path('<int:pk>/', JobDetailView.JobDetailView.as_view(),name='job-detail'),
    
    path('Search/', views.JobsByRegion ,name='job-filter'),

    #ajax url
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities') , 

    #api urls
    path('api/Job/allJobs/', AllJobsList.as_view(), name='api-job-alljobs') ,
    path('api/job/<int:pk>/', JobById.as_view(), name='api-job-by-id'),
]
