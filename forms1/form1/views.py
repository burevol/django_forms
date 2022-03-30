from django.shortcuts import render
from django.views.generic import ListView, FormView

from .models import Questions, Category
from .forms import QuestionForm

# Create your views here.

class CategoryView(ListView):
    model = Category
    template_name = 'form1/categories.html'


class QuestionView(FormView):
    template_name = 'form1/question.html'
    form_class = QuestionForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['category'] = Category.objects.get(pk=self.kwargs['pk'])
        return kwargs






