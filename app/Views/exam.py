from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.db.models import F

from app.models import Module, Result, Answer_Sheet

@login_required(login_url='login')
def Exam(request, m, i):
    module = Module.objects.get(id=m)

    if i <= 0:
        R = Result.objects.create(user=request.user, module=module, marks=0)
    R = Result.objects.latest('time')
    
    if request.method == 'POST':
        ans = request.POST.get('opt')

        prevQ = module.question_set.all()[i-1]
        if ans == str(prevQ.Correct):
            Answer_Sheet.objects.create(Q=prevQ,Result=R,right=True,Attempted_option=ans)
            R.marks = F('marks')+1
            R.save()
        else:
            Answer_Sheet.objects.create(Q=prevQ,Result=R,right=False,Attempted_option=ans)

        if i >= module.questions:
            return redirect('dashboard', request.user.id)

        question = module.question_set.all()[i]
        i=i+1
        context = {'Module':module, 'Q':question, 'i':i}
        return render(request, 'app/Other/Exam.html', context)
        
    question = module.question_set.all()[i]
    i=i+1
    context = {'Module':module, 'Q':question, 'i':i}
    return render(request, 'app/Other/Exam.html', context)