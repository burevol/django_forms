from django import forms
from .models import Questions, Category


class QuestionForm(forms.Form):
    question = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple, required=False)

    def __init__(self, *args, category, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question'].queryset = Questions.objects.filter(category=category)
        self.fields['question'].label = category.cat