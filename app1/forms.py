from django.forms import ModelForm
from app1.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title' , 'status' , 'priority']
