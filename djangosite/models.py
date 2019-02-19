from django.db import models
from django.shortcuts import render


#importing loading from django template
from django.template import loader
from django.http import HttpResponse



class Employee(models.Model):  
    eid = models.CharField(max_length=20,null=True,blank=True) 
    ename = models.CharField(max_length=100,null=True,blank=True)  
    econtact = models.CharField(max_length=15,null=True,blank=True)  
    class Meta:  
        db_table = "employee" 

class Student(models.Model):

	first_name=models.CharField(max_length=20,null=True,blank=True)
	last_name =models.CharField(max_length=30,null=True,blank=True)
	contact	  =models.IntegerField()
	email2  =models.EmailField(max_length=50,null=True,blank=True)
	age    =models.IntegerField()

def index(request):
	template=loader.get_template('index.html')#getting our template
	return HttpResponse(template.render()) #rendering the template in HttpResponse

class Meta:
	db_table="student"