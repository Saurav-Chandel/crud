from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

#this function will ad new item and show all items
def add(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
             nm=fm.cleaned_data['name']
             em=fm.cleaned_data['email']
             ps=fm.cleaned_data['password']
             reg=User(name=nm,email=em,password=ps)
             reg.save()
             #fm.save()
             fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all().order_by('-id')

    return render(request,'add_and_start.html',{'form':fm,'stu':stud})


#this function will update and edit
def updatedata(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'update.html',{'form':fm})


#this function will delete
def delete(request,id):
  if request.method=="POST":
      pi=User.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/')