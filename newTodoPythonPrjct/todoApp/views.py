from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'tsk'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs= {'pk':self.object.id})

class TaskdeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvindex')



def add(request):
    tk = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(name = name, priority = priority, date= date)
        task.save()
    return render(request,'index.html',{'task':tk})

# def details(request):
#     tk = Task.objects.all()
#     return  render(request,'detail.html',{'task':tk})


def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/index')
    return render(request,'delete.html')

def update(request,id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/index')
    return render(request,'edit.html',{'fm':f, 'task':task})

# Create your views here.
