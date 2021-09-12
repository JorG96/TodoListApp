from django.db import models

class TodoList(models.Model):
    txt=models.CharField(max_length=50)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.txt
    