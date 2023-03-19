from tasks.models import Task, TaskCategory
from django import forms

class TaskForm(forms.ModelForm):
	description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
	category = forms.ModelChoiceField(queryset=TaskCategory.objects.all())
	class Meta():
		model = Task
		fields = ('description', 'category')