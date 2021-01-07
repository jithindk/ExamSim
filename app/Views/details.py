from django.shortcuts import render
from django.db.models import Max

from app.models import Course, Module, Result, Taken

def Course_Details(request, pk):
    course = Course.objects.get(id=pk)
    modules = course.module_set.all()

    context = {'Course':course, 'Modules':modules}
    return render(request, 'app/Details/course.html',context)

def Module_Details(request, pk):
    module = Module.objects.get(id=pk)
    questions = module.question_set.all()
    context = {'Module':module, "Q":questions}
    return render(request, 'app/Details/module.html',context)

def Result_Details(request, pk):
    result = Result.objects.get(id=pk)
    answers = result.answer_sheet_set.all()
    n = list(range(answers.count()))

    context = {'Result':result, 'Answers':answers, 'n':n}
    return render(request, 'app/Details/result.html', context)

def Taken_Courses(request, pk):
    t = Taken.objects.get(id=pk)
    course = t.course.name
    modules = t.course.module_set.all()
    n = modules.count()
    attempts = [0 for i in range(n)]
    high = [0 for i in range(n)]
    for i in range(n):
        results = modules[i].result_set.filter(user__exact=t.user)
        attempts[i] = results.count()
        high[i] = results.aggregate(Max('marks'))['marks__max']

    context = {"Course":course, "Modules":modules, "Attempts":attempts, "HighScore":high}
    return render(request, 'app/Details/yourCourses.html', context)
