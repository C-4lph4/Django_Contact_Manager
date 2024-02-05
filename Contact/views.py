from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact

# Create your views here.


def index(request):
    contact=Contact.objects.all()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        return render(request, "index.html",{"form":ContactForm,'contacts':contact})
