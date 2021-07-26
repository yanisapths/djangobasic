from django.shortcuts import render

#ส่งreq,respข้อมูลกลับไป จาก http เรียกใช้งานฟังก์ชัน hello
#from django.http import HttpResponse

# Create your views here. example
   #def hello(request):
  #return HttpResponse("<h2>HelloWorld</h2>")

def hello(request):
  rating=4
  tags = ['study','design','lifestyle']
  return render(request,'site.html',
    {'name' : 'ME LIVING',
    'author' : 'Dookdik',
    'tags' : tags,
    'rating': rating
    })

def page1(request):
  return render(request,'page1.html') 

def createform(request):
    return render(request,'form.html')

def addBlog(request):
  name = request.POST['name']
  description = request.POST['description']
  return render(request,'result.html',{'name':name,'description':description})