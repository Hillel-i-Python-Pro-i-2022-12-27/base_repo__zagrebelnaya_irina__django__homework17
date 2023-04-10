from django.forms import ModelForm

from apps.contact_us.models import ContactUs


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ["email", "name", "phone", "question"]
