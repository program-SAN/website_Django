from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

#{this is used for seding variable to a page}
#def index(request):
#   context = {
#       "var":" this is sent"
#   }
#   return render(request,'index.html',context)
    #return HttpResponse('this is homepage')

def index(request):
    return render(request,'index.html' )

def about(request):
    return render(request,'about.html' )
    #return HttpResponse('this is aboutpage')

def services(request):
    return render(request,'services.html' )
    #return HttpResponse('this is servicespage')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('message')
        contact = Contact(name=name,email=email,text=text,date=datetime.today())
        contact.save()
        messages.success(request, "Message has been sent.")

    return render(request,'contact.html' )
    #return HttpResponse('this is contactpage')