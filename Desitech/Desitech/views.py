from django.shortcuts import render , HttpResponse , redirect
from jobs.models import Job
from accounts.forms.ContactForm import contactUs
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



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


login_decorator = login_required (login_url = 'accounts:login')
@method_decorator(login_decorator, name='dispatch')
class Contact (View) :

    def get (self , request):
        
        contact_form = contactUs()
        context = {'page_title' : 'contact' , 'contact_form' : contact_form}
        return render (request , 'contact.html' , context)

    def post (self , request):
        contact_form = contactUs(request.POST)
        if  contact_form.is_valid():
             
                contact = contact_form.save(commit=False)

                contact.Sent_by_id = request.user.id
                contact.save()

                return redirect ('/' )
        else:
            context = {'page_title' : 'contact' , 'contact_form' : contact_form}
            return render (request , 'contact.html' , context)
