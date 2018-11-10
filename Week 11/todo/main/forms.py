from django.forms import ModelForm
from main.models import Task, Author

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['list_name', 'task_order', 'created_at', 'due_on', 'owner', 'mark']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email')