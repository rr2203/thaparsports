from django.db import models


class imagegallery(models.Model):
    title=models.CharField(max_length=200)
    image1=models.FileField(null=True,blank=True)
    image2=models.FileField(null=True,blank=True)
    image3=models.FileField(null=True,blank=True)
    image4=models.FileField(null=True,blank=True)
    image5=models.FileField(null=True,blank=True)
    image6=models.FileField(null=True,blank=True)


    def __str__(self):
        return (self.title)