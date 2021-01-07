from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from app.Forms import CreateUser_Form, Course_Form, User_Form, Module_Form, Question_Form
from app.Decorators import user_notlive
from app.models import User, Course, Module, Question

@user_notlive
def Register(request):
    form = CreateUser_Form()

    if request.method == 'POST':
        form = CreateUser_Form(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            messages.success(request, "User "+user+" Created Successfully")
            form.save()
            user = User.objects.latest("date_joined")
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            return redirect('login')

    context = {"form": form}
    return render(request, 'app/Forms/User/Register.html', context)


@user_notlive
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard', user.id)
        else:
            messages.info(request, "Incorrect Username or Password")
    
    return render(request , 'app/Forms/User/Login.html')

@login_required(login_url='login')
def Update_User(request):
    user = request.user
    form = User_Form(instance=user)

    if request.method == 'POST':
        form = User_Form(request.POST, instance=user)
        if form.is_valid:
            form.save()
            return redirect("dashboard", request.user.id)

    context = {'form': form}
    return render(request, 'app/Forms/User/editProfile.html',context)

@login_required(login_url='login')
def Password_Reset(request):
    form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Password successfully reset!')
            return redirect('login')
        else:
            errors = '\n'.join([str(e) for e in form.error_messages.values()])
            messages.error(request, errors)

    context = {'form':form}
    return render(request, 'app/Forms/User/Password_reset.html', context)

@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def Delete_User(request):
    user = request.user
    
    if request.method == 'POST':
        user.delete()
        return redirect('/')
    
    context = {'name':'User', 'item': user.username}
    return render(request, 'app/Forms/delete.html',context)



@login_required(login_url='login')
def Create_Course(request, pk):
    user = User.objects.get(id=pk)
    form = Course_Form(initial={'author':user})

    if request.method == 'POST':
        form = Course_Form(request.POST)
        if form.is_valid:
            form.save()
            course = Course.objects.latest('id')
            return redirect("courseDetails", course.id)

    context = {'form': form, 'user':user}
    return render(request, 'app/Forms/CreateCourse.html',context)

@login_required(login_url='login')
def Update_Course(request, pk):
    course = Course.objects.get(id=pk)
    form = Course_Form(instance=course)

    if request.method == 'POST':
        form = Course_Form(request.POST, instance=course)
        if form.is_valid:
            form.save()
            return redirect("dashboard", request.user.id)

    context = {'form':form, 'name':'course', 'item':course.name}
    return render(request, 'app/Forms/update.html',context)

@login_required(login_url='login')
def Delete_Course(request, pk):
    course = Course.objects.get(id=pk)

    if request.method == 'POST':
        course.delete()
        return redirect("dashboard", request.user.id)

    context = {'name':'Course', 'item': course}
    return render(request, 'app/Forms/delete.html',context)



@login_required(login_url='login')
def Create_Module(request, pk):
    course = Course.objects.get(id=pk)
    form = Module_Form(initial={'course':course})

    if request.method == 'POST':
        form = Module_Form(request.POST)
        if form.is_valid():
            form.save()
            module = Module.objects.latest('id')
            return redirect('moduleDetails', module.id)

    context = {"form":form, "Course":course}
    return render(request, 'app/Forms/CreateModule.html', context)

@login_required(login_url='login')
def Update_Module(request, pk):
    module = Module.objects.get(id=pk)
    form = Module_Form(instance=module)

    if request.method == 'POST':
        form = Module_Form(request.POST, instance=module)
        if form.is_valid:
            form.save()
            return redirect("moduleDetails", module.id)

    context = {'form': form, 'name':'module', 'item':module.name}
    return render(request, 'app/Forms/update.html',context)

@login_required(login_url='login')
def Delete_Module(request, pk):
    module = Module.objects.get(id=pk)

    if request.method == 'POST':
        c = module.course
        module.delete()
        return redirect("courseDetails", c.id)

    context = {'name':'Module', 'item': module}
    return render(request, 'app/Forms/delete.html',context)



@login_required(login_url='login')
def Create_Question(request, pk):
    module = Module.objects.get(id=pk)
    form = Question_Form(initial={'module':module})

    if request.method == 'POST':
        form = Question_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('moduleDetails', module.id)

    context = {"form":form, "Module":module}
    return render(request, 'app/Forms/CreateModule.html', context)

@login_required(login_url='login')
def Update_Question(request, pk):
    q = Question.objects.get(id=pk)
    form = Question_Form(instance=q)

    if request.method == 'POST':
        form = Question_Form(request.POST, instance=q)
        if form.is_valid:
            form.save()
            return redirect("moduleDetails", q.module.id)

    context = {'form': form, 'name':'This Question', 'item':""}
    return render(request, 'app/Forms/update.html',context)

@login_required(login_url='login')
def Delete_Question(request, pk):
    q = Question.objects.get(id=pk)

    if request.method == 'POST':
        m = q.module
        q.delete()
        return redirect("moduleDetails", m.id)

    context = {'name':'Module', 'item': q.Q}
    return render(request, 'app/Forms/delete.html',context)