from django.db import models

class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username

class Note(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    datetime=models.DateTimeField('date published')
    note=models.CharField(max_length=500)
    title=models.CharField(max_length=50)
    upload=models.ImageField(upload_to='media/', blank=True)
    editdate =models.DateTimeField('date edited'  )

    def __str__(self):
        return self.title


class Bin(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    note=models.CharField(max_length=200)
    datetime=models.DateTimeField('date created')
    deletedate=models.DateTimeField('date deleted')
    def __str__(self):
        return self.title
# Create your models here.
