from django.db import models
from accounts.models.User import User
from accounts.models.Country import Country
from accounts.models.City import City
from datetime import datetime

# Create your models here.



class Job (models.Model):

    publish_By =models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=50) 
    abstract = models.TextField()
    skills = models.TextField()
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    job_manger = models.Manager()

    def get_days_ago (self):
        return  datetime.now().day - self.date.day  
       