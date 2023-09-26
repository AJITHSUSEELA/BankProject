from django.urls import path
from .views import *

urlpatterns=[
    path('login/',login),
    path('register/',register),
    path('profile/',profile),
    path('edit/<int:id>',edit),
    path('imgedit/<int:id>',imgedit),
    path('addamount/<int:id>',addamount1),
    path('success/',success),
    path('withdraw/<int:id>',withdraw),
    path('success2/',success2),
    path('balance/<int:id>',balance),
    path('success3/',success3),
    path('mini/<int:id>',mini),
    path('depdisplay/', depdisplay),
    path('withdisplay/',withdisplay),
    path('adminhtml/',adminhtml),
    path('adminlogin/',adminlogin),
    path('adminprofile/',adminprofile),
    path('newsdisplay/',newsdisplay),
    path('admnewsdisp/',admnewsdisp),
    path('newsdelete/<int:id>',newsdelete),
    path('newsedit/<int:id>',newsedit),
    path('wish/<int:id>',wish),
    path('wishmodeldisp/',wishmodeldisp),
    path('logout_view/',logout_view),
    path('forget_password/',forget_password),
    path('change/<int:id>',change),
    path('moneytransfer/<int:id>',moneytransfer)

]