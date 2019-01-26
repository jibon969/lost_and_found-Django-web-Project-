from django.db import models
from home.models import MyUser


# Create your models here.


class Person(models.Model):
    status = models.CharField(max_length=60)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")

    PERSON_CHOICES = (
        ('F', 'Found Person'),
        ('L', 'Lost Person'),
    )
    person = models.CharField(max_length=1, choices=PERSON_CHOICES, default="Found Item")
    age = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    body_color = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=16)
    image = models.FileField()
    identification_mark = models.TextField(help_text='Separate each item by comma')
    secret_information = models.TextField(help_text='Separate each item by comma')
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ["-update"]

    def get_contents(self):
        return self.identification_mark.split(",")

    def get_excludes(self):
        return self.secret_information.split(",")
