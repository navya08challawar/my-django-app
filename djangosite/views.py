from django.shortcuts import render
import datetime 
import csv 
#importing loading from django template
from django.template import loader
from djangosite.form import StuForm,EmployeeForm
from reportlab.pdfgen import canvas
# Create your views here.
from django.http import  HttpResponse,HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from djangosite.functions.functions import handle_uploaded_file  


def hello(request):

	return HttpResponse("<h2>Hello,Welcome to Django!</h2>")


def index(request):  
    if request.method == 'POST':  
        student = StuForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StuForm()  
        return render(request,"index.html",{'form':student})

def emp(request):
	if request.method == "POST":  
	    form = EmployeeForm(request.POST)  
	    if form.is_valid():  
	        try:  
	            return redirect('/')  
	        except:  
	            pass  
	else:  
	    form = EmployeeForm()  
	return render(request,'index.html',{'form':form})
	
@require_http_methods(["GET"])
def show(request):
	return HttpResponse('<h1>This is Http GET request.</h1>')

def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    return response  
def getpdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['content-Disposition']='attachment;filename="file.pdf"'
    p=canvas.Canvas(response)
    p.setFont("Times-Roman",55)
    p.drawString(100,700,"Hello,javatpoint.")
    p.showPage()
    p.save()
    return response