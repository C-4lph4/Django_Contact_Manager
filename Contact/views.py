from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact

# Create your views here.


def index(request):
    contact = Contact.objects.all()
    if request.method == "POST":
        if "edit" in request.POST:
            pk = request.POST.get("edit")

            contact_obj = Contact.objects.get(pk=pk)
            editForm = ContactForm(instance=contact_obj)
            return render(
                request,
                "index.html",
                {"editForm": editForm, "contacts": contact, "contact_id": pk},
            )
        elif "edited" in request.POST:
            pk=request.POST.get("edited")
            contact_obj = Contact.objects.get(pk=pk)
            editedForm = ContactForm(request.POST, instance=contact_obj)
            if editedForm.is_valid:
                editedForm.save()
            return redirect("/")

        else:
            AddForm = ContactForm(request.POST)
            if AddForm.is_valid():
                AddForm.save()

            return redirect("/")
    else:

        addForm = ContactForm()
        return render(request, "index.html", {"addForm": addForm, "contacts": contact})





def delete(request, pk):
    contact_obj = get_object_or_404(Contact, id=pk)
    contact_obj.delete()
    return redirect("/")
