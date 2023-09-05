from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_liabrary(request):
    lo=liabrary.objects.all()
    d={'lo':lo}
    if request.method=='POST':
        s=request.POST['sa']
        so=liabrary.objects.get_or_create(section=s)[0]
        so.save()
        return render(request, 'display_liabrary.html',d)

    return render (request,'insert_liabrary.html',)

def insert_book(request):
    bo=books.objects.all()
    so=liabrary.objects.all()
    d1={'bo':bo, 'so':so}

    if request.method=="POST":
        se=request.POST['se']
        bn=request.POST['bn']
        a=request.POST['a']
        so=liabrary.objects.get(section=se)
        bo=books.objects.get_or_create(section=so,bname=bn, auther=a)[0]
        bo.save()
        return render(request, 'display_books.html',d1)

    return render (request,'insert_book.html',d1)
    
