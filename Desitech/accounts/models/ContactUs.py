from django.db import models
from accounts.models.User import User
from datetime import datetime


class ContactUs  (models.Model):

    Sent_by =models.ForeignKey(User , on_delete=models.CASCADE)
    Subject = models.CharField(max_length=50) 
    Message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Users Messages"

      

       