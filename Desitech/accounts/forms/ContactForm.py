from django import forms
from accounts.models.ContactUs import ContactUs


class contactUs (forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ("Subject" , 'Message' ,)
        labels= { 
                'Subject': 'Subject', 
                'Message': 'Message',
                }

        widgets = {
            'Subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Subject"}),
            'Message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Write your Message here" , 'style':'resize: none;'}), 
            }






