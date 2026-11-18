from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    email=models.IntegerField()
    age=models.IntegerField()
    department = models.CharField(max_length=100)
    def _str_(self):
        return self.name