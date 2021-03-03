from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=80)


# get_absolute_url(): Its the replacement for success_url attribute in views.py. This method is written
# in models.py file and it's for redirection purpose
