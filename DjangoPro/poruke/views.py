from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(reques):
    return HttpResponse('Zdravo')

def number(request , broj = 69):
    return HttpResponse('Broj: ' + str(broj))


def word(request,rec):
    return HttpResponse('Rec: ' + rec)

def params(request):
    return HttpResponse('Params:' + str([str(k) + " : "  + str(v)  for k,v in request.GET.items()]))

def regex(request , godina , mesec):
    return HttpResponse('Godina:' + godina + ' Mesec:' + mesec);

def hello(request):
    return render(request , 'poruke/hello.html')
    return HttpResponse()