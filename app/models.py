from django.db import models

# Create your models here.

class liabrary(models.Model):
    section=models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return self.section

class books(models.Model):
    section=models.ForeignKey(liabrary, on_delete=models.CASCADE)
    bname=models.CharField(max_length=100, primary_key=True)
    auther=models.CharField(max_length=100)
    
    def __str__(self):
        return self.bname
