from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.


def index(request):
    contacts = Contact.objects.all()
    if request.method == "POST":
        if "edit" in request.POST:
            pk = request.POST.get("edit")

            contact_obj = Contact.objects.get(pk=pk)
            editForm = ContactForm(instance=contact_obj, initial={"picture": "/"})
            return render(
                request,
                "index.html",
                {
                    "editForm": editForm,
                    "contacts": contacts,
                    "contact_id": pk,
                    "picture": contact_obj.picture.url,
                },
            )
        elif "edited" in request.POST:
            pk = request.POST.get("edited")
            contact_obj = Contact.objects.get(pk=pk)
            editedForm = ContactForm(request.POST, request.FILES, instance=contact_obj)
            if editedForm.is_valid:
                editedForm.save()
            return redirect("/")

        else:
            AddForm = ContactForm(request.POST, request.FILES)
            if AddForm.is_valid():
                AddForm.save()

            return redirect("/")
    else:
        addForm = ContactForm()
        if "query" in request.GET:
            query = request.GET.get("query")
            contacts = (
                Contact.objects.filter(name__icontains=query)
                if query
                else Contact.objects.all()
            )

        return render(request, "index.html", {"addForm": addForm, "contacts": contacts})


def delete(request, pk):
    contact_obj = get_object_or_404(Contact, id=pk)
    contact_obj.delete()
    return redirect("/")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user != None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")
    else:
        return render(request, "login.html")
