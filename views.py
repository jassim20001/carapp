from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
      cars=Carsone.objects.all()
      cars2=Carstwo.objects.all()
      serves=Serves.objects.all()

      context={
        'cars':cars,
        'cars2':cars2,
        'serves':serves
    }


      return render(request,'home.html',context=context)


def conect(request):
    if request.method=='POST':
         name=request.POST['name']
         email=request.POST['email']
         message=request.POST['msg']
         conect=Conect.objects.create(name=name,email=email,message=message)
         conect.save()
         return render(request,'conect.html',{'conect':conect})
    
     
    return render(request,'conect.html')

def detalcar(request,slug):
    car=Carsone.objects.get(slug=slug)
    context={
        'cars':car
    }

    return render(request,'detalcars.html',context=context)

