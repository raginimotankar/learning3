from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Hello world!")
    #return render(request,'index.html')
    #a={'myvalue':'Python'}   
    return render(request,'index.html',{'myvalue':'Python','myvalue1':'Ragini','myvalue2':'Nagpur'})
