from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app.Filters import Filter_Course, Filter_Result

from app.models import Course, User

def Home(request):
    return render(request, 'app/Main/Home.html')

def About(request):
    return render(request, 'app/Main/About.html')

def Courses(request):
    searchFilter = Filter_Course(request.GET, queryset=Course.objects.all())
    courses = searchFilter.qs

    context = {'Courses':courses, "searchFilter": searchFilter}
    return render(request, 'app/Main/Courses.html', context)

@login_required(login_url='login')
def Dashboard(request,pk):
    user = User.objects.get(id=pk)
    courses = user.course_set.all()
    results = user.result_set.order_by('id').reverse()
    taken = user.taken_set.all()
    C_len = len(courses)
    T_len = len(taken)
    R_len = len(results)

    context = {'user':user, "Courses":courses, 'Results':results, 'Taken':taken, 'C_len':C_len, 'T_len':T_len, 'R_len':R_len}
    return render(request, 'app/Main/Dashboard.html', context)

@login_required(login_url='login')
def Your_Courses(request, pk):
    u = User.objects.get(id=pk)
    taken = u.taken_set.all()

    context = {'Taken':taken}
    return render(request, 'app/Main/Your_courses.html', context)

@login_required(login_url='login')
def Results(request, pk):
    u = User.objects.get(id=pk)
    #searchFilter = Filter_Result(request.GET, queryset=u.result_set.all().order_by('time').reverse())
    #results = searchFilter.qs
    results = u.result_set.all().order_by('time').reverse()

    context = {'Results':results} #'searchFilter':searchFilter}
    return render(request, 'app/Main/Results.html', context)