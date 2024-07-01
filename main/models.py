from django.db import models
from account.models import User
from autoslug import AutoSlugField

# Create your models here.
class Project(models.Model):
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    employee = models.ManyToManyField(User, related_name="projects")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name
    
    
class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    employee = models.ManyToManyField(User, related_name="task")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_task')
    status = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name
    