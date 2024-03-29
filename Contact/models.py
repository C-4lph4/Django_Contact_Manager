from django.db import models


# Create your models here.
class Contact(models.Model):
    picture = models.ImageField(upload_to='profile_img',default='blank.png')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
