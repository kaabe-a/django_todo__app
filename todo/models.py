from django.db import models
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self,*args):
        return reverse('todo:todo_detail',args=[self.slug])
    