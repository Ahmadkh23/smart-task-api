from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('low' , 'Low'),
        ('medium' , 'Medium'),
        ('high' , 'High'),
    )

    title = models.CharField(max_length = 255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length = 10 , choices = PRIORITY_CHOICES , default = 'medium')
    due_date = models.DateTimeField(null=True , blank = True)

    created_at = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User , related_names = 'tasks' , on_delete = models.CASCADE)

    def __str__(self):
        return self.title