from django.db import models
# from .views import TodoModel

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    def __str__(self):
        return self.title