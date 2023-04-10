from django.urls import path

from apps.contact_us import views

app_name = "contactus"

urlpatterns = [
    path("contactus/", views.create, name="index"),
]
