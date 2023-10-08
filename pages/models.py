from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=20)
    txt1 = models.CharField(max_length=20)
    txt2 = models.CharField(max_length=20)
    img = models.ImageField(upload_to="picture")
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class About(models.Model):
    name = models.CharField(max_length=20)
    prof = models.CharField(max_length=25)
    desc = models.TextField(blank=False)
    img = models.ImageField(upload_to='about')
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Skills(models.Model):
    name = models.CharField(max_length=40)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

# Create your models here.