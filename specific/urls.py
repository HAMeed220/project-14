from specific.views import *
from django.urls import path

app_name= 'specific'

urlpatterns = [
    path('parvathidevi/',parvathidevi,name='parvathidevi'),
    path('karthikaya/',karthikaya,name='karthikaya'),
]
