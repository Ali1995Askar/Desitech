from django.shortcuts import render , HttpResponse , redirect
from jobs.models import Job

def index (request):
  
    randomText = 'some text or any info'
    list_text = []
    happy_clients = [1,2,3]
  
    for i in range (5):
        list_text.append (randomText)
    context = {'page_title' : 'home' , 'text' : list_text , 
                'happy_clients' : happy_clients , 'job_post' : 1000 , 
                'clients' : 1400 , 'job_filled' : 700 , 'companies' : 400}
    return render (request , 'home.html' , context   )

def about (request):
    context = {'page_title' : 'about'}
    return render (request , 'about.html' ,context)

def contact (request):
    context = {'page_title' : 'contact'}
    return render (request , 'contact.html' , context)