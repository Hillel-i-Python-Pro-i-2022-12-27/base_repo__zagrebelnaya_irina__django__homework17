from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=13, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    question = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.phone} - {self.email} - {self.question}"

    __repr__ = __str__
