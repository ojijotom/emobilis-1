from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=50)
    adm=models.IntegerField()
    date=models.DateField()
    form=models.CharField(max_length=50)



    def __str__(self):
        return self.name
class Teachers(models.Model):
    name=models.CharField(max_length=15)
    age=models.IntegerField()
    email=models.EmailField()
    department=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return self.name+" "+self.status

class Parents(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    email=models.EmailField()
  

    def __str__(self):
        return self.firstname+" "+self.lastname


