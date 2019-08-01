from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect
from . import models
def index(request):
    questions_list = models.Question.objects.order_by('-pub_date')
    context = {'questions_list' : questions_list}
    return render(request,'polls/index.html',context)

def details(request,pk):
    question = get_object_or_404(models.Question,pk=pk)
    return render(request,'polls/details.html',{'question':question})
def results(request,pk):
    question = get_object_or_404(models.Question,pk=pk)
    return render(request,'polls/result.html',{'question':question})

def vote(request,pk):
    question = get_object_or_404(models.Question,pk=pk)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        pass
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
