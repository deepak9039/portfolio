from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(max_length=50, verbose_name="Email")
    number = models.CharField(max_length=50, verbose_name="Phone Number")
    message = models.TextField(max_length=200, verbose_name="Message")

    def __str__(self):
        return self.first_name