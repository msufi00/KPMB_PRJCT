from django.shortcuts import render
from registration.models import Course
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def testing(request):
    mycourse = Course.objects.all().values()
    context = {
        'mycourse':mycourse,
    }
    return render (request,"index.html",context)

# Create your views here.
def index(request):
    context = {
        'firstname':'Sufi Arif',
    }
    return render (request,"index.html",context)

# def course(request):
#     if request.method == 'POST':
#         c_code = request.POST['code']
#         c_desc = request.POST['desc']
#         c_date = request.POST['date']
#         data = Course(coursecode=c_code, coursename=c_desc, coursedate=c_date)
#         data.save()
#         dict = {
#             'message': 'Data Saved'
#         }
#         return render(request, 'course.html', dict)
#     else:
#         dict = {
#             'message': ''
#         }
#         return render(request, 'course.html', dict)
    

def new_course(request):

    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        c_date = request.POST['date']
        data = Course(coursecode=c_code, coursename=c_desc, coursedate=c_date)
        data.save()
        dict = {
            'message': 'Data Save'
        }
        return render(request, 'course.html', dict)
    else:
        dict = {
            'message': ''
        }
        return render(request, 'course.html', dict)
    
def course(request):
    alldata = Course.objects.all()
    dict = {
        'alldata':alldata
    }
    return render(request,'vcourse.html',dict)

def searchpage(request):
    search_value = request.GET.get('search')
    members = Course.objects.filter(Q(coursecode=search_value))
    return render(request, 'searchpage.html', {'members': members})

def update(request,coursecode):
    data = Course.objects.get(coursecode=coursecode)
    dict={
        'data':data
    }
    return render(request,'update.html',dict)

def updatedata(request,coursecode):
    c_desc = request.POST['desc']
    data = Course.objects.get(coursecode=coursecode)
    data.coursename = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))


