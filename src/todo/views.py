from django.views.generic import TemplateView,ListView,DetailView,DeleteView
from django.views.generic.edit import CreateView,UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from .models import Todo

class HomePageView(TemplateView):
    template_name = 'home.html'


class TodoListView(LoginRequiredMixin,ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'


class TodoDetailView(LoginRequiredMixin,DetailView):
    model = Todo
    template_name = 'todo_detail.html'
    context_object_name = 'todo'

class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = Todo
    template_name = 'todo_edit.html'
    fields = ('title','body','completed')

class TodoDeleteView(LoginRequiredMixin,DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo_list')

class TodoCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    template_name = 'todo_new.html'
    fields = ('title','body')

    def form_valid(self,form):
        model = form.save(commit=False)
        model.author = self.request.user
        model.save()
        
        return super().form_valid(form)