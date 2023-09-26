from django import forms

class registerform(forms.Form):
    firstname= forms.CharField(max_length=30)
    lastname= forms.CharField(max_length=30)
    uname= forms.CharField(max_length=20)
    email= forms.EmailField()
    phone= forms.IntegerField()
    photo= forms.FileField()
    pin= forms.IntegerField()
    repin= forms.IntegerField()

class loginform(forms.Form):
    uname=forms.CharField(max_length=30)
    pin= forms.IntegerField()


class adminform(forms.Form):
    topic=forms.CharField(max_length=300)
    content=forms.CharField(max_length=3000)

class adminlogform(forms.Form):
    username=forms.CharField(max_length=30)
    password = forms.IntegerField()


# class moneyform(forms.Form):
#     name= forms.CharField(max_length=20)
#     acc = forms.IntegerField()
#     amount = forms.IntegerField()

