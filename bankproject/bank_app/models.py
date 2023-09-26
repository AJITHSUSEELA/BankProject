from django.db import models

# Create your models here.

class registermodel(models.Model):
    firstname= models.CharField(max_length=30)
    lastname= models.CharField(max_length=30)
    uname= models.CharField(max_length=20)
    email= models.EmailField()
    phone= models.IntegerField()
    photo= models.FileField(upload_to='bank_app/static')
    pin= models.IntegerField()
    balance=models.IntegerField()
    acc=models.IntegerField()

class loginmodel(models.Model):
    uname= models.CharField(max_length=30)
    pin= models.IntegerField()

#deposit view
class addamount(models.Model):
    # choice=[
    #     ('withdraw','withdraw'),
    #     ('deposit','deposit')
    # ]
    amount=models.IntegerField()
    date= models.DateField(auto_now_add=True)
    uid = models.IntegerField()
    # withdraw=models.CharField(max_length=30,choices=choice)
    # statement=models.

class withdrawamount(models.Model):
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    uid = models.IntegerField()


class mini(models.Model):
    choice=[
        ('withdraw','withdraw'),
        ('deposit','deposit')
    ]
    statement=models.IntegerField(choices=choice)


class adminmodel(models.Model):
    topic=models.CharField(max_length=300)
    content=models.CharField(max_length=3000)
    date=models.DateField(auto_now_add=True)

class wishlist(models.Model):
    Uid=models.IntegerField()
    newsid=models.IntegerField()
    topic = models.CharField(max_length=300)
    content = models.CharField(max_length=3000)
    date = models.DateField()


class moneymodel(models.Model):
    name= models.CharField(max_length=20)
    acc = models.IntegerField()
    amount = models.IntegerField()


