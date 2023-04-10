from django.contrib import messages
from django.core.checks import CRITICAL
from django.shortcuts import render, redirect

from apps.contact_us.forms import ContactUsForm


def create(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if not (request.POST.get("name").isalpha()):
            messages.add_message(request, CRITICAL, "Name must have only letters.")
            return redirect("contactus:index")
        if not (request.POST.get("phone").isdigit()):
            messages.add_message(request, CRITICAL, "Phone must have only numbers.")
            return redirect("contactus:index")
        if not (request.POST.get("email")):
            messages.add_message(request, CRITICAL, "Email must be not empty.")
            return redirect("contactus:index")
        if form.is_valid():
            form.save()
            messages.add_message(request, CRITICAL, "Your message was added.")
            return redirect("contactus:index")
    else:
        form = ContactUsForm()

        return render(request, "contact_us/form.html", {"form": form})
