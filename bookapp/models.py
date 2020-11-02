from django.db import models



class Book(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    isbn=models.CharField(max_length=255,blank=True,null=True)
    authors=models.CharField(max_length=255,blank=True,null=True)
    publisher=models.CharField(max_length=255,blank=True,null=True)
    country=models.CharField(max_length=255,blank=True,null=True)
    released=models.CharField(max_length=255,blank=True,null=True)
    numberOfPages=models.IntegerField(max_length=10)

    def __str__(self):
        return self.all


