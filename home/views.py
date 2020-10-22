from django.shortcuts import render
from .models import Contact
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            number = request.POST['number']
            email = request.POST['email']
            message = request.POST['message']
            contact_us = Contact(first_name=first_name,last_name=last_name,number=number,email=email,message=message)
            contact_us.save()
            messages.success(request,"Your Message is Recorded. We anser within 24 hours ! ")
    return render(request,'home.html')