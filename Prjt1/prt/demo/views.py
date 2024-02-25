from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    name="india"
    return render(request,"index.html",{'obj':name})

def addition(request):
    N1=int(request.GET['num1'])
    N2=int(request.GET['num2'])
    sum=N1+N2
    sub=N1-N2
    multi=N1*N2
    return render(request,"result.html",{'sum':sum,'sub':sub,'multi':multi})





