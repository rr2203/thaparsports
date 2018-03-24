from django.db import models

# Create your models here.






        
class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.FileField(null=True,blank=True)
    name = models.CharField(max_length=200,default=" ")
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    content=models.TextField(null=True)
    side=models.TextField(null=True)

    def __str__(self):
        return (self.title)

class r_Post(models.Model):
    title=models.CharField(max_length=200)
    image1=models.FileField(null=True,blank=True)
    image2=models.FileField(null=True,blank=True)
    image3=models.FileField(null=True,blank=True)
    image4=models.FileField(null=True,blank=True)
    name = models.CharField(max_length=200,default=" ")
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    content=models.TextField(null=True)
    side=models.TextField(null=True)

    def __str__(self):
        return (self.title)

class achPost(models.Model):
    title=models.CharField(max_length=200)
    image=models.FileField(null=True,blank=True)
    name = models.CharField(max_length=200,default=" ")
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    content=models.TextField(null=True)
    side=models.TextField(null=True)

    def __str__(self):
        return (self.title)

