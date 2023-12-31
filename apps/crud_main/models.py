from django.db import models

class Todo(models.Model):
    done = models.BooleanField(default=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self) -> str:
    #     return super().__str__()
