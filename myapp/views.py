from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request,"index.html",{})

def contact_view(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            message=request.POST.get("message")
        )
    return render(request,"contact.html")    
