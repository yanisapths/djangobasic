from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
#ส่งreq,respข้อมูลกลับไป จาก http เรียกใช้งานฟังก์ชัน hello
#from django.http import HttpResponse

# Create your views here. example
   #def hello(request):
  #return HttpResponse("<h2>HelloWorld</h2>")

def hello(request):
   #Queryข้อมูลdata จากตัวmodel ให้import Post จาก models.py มาด้วย
  data = Post.objects.all()
  return render(request,'site.html',{'posts':data})

def page1(request):
  return render(request,'page1.html') 

def register(request):
    return render(request,'form.html')

def addUser(request):
  username = request.POST['username']
  firstname = request.POST['firstname']
  lastname = request.POST['lastname']
  email = request.POST['email']
  password = request.POST['password']
  repassword = request.POST['repassword']

  user=User.objects.create_user(username=username,password=password, email=email,first_name=firstname,last_name=lastname)
  user.save()
  return render(request,'result.html')
         

      
