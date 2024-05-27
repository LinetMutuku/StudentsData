import os
import uuid

from django.db import models


def unique_img_name(instance, filename):
    name = uuid.uuid4()
    print(name)

    ext = filename.split('.')[-1]
    full_name = f'{name}.{ext}'
    return os.path.join('students', full_name)


# Create your models here.


class Student(models.Model):
    name= models.CharField(max_length=100)
    adm_no= models.IntegerField(unique=True)
    dob = models.DateField(null=True)
    profile_picture = models.ImageField(upload_to=unique_img_name, null=True, default='students/students.png')
    disabled = models.BooleanField(default=False)
   


    def __str__(self):
        return self.name


