from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100,  blank=False)
    description = models.CharField(blank=True)
    date = models.DateField(blank=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title