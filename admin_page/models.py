from pyexpat import model
from tabnanny import verbose
from django.db import models
import uuid

# Create your models here.

class Criminal(models.Model):
    criminal_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=256)
    age = models.IntegerField(null=False)
    sex = models.CharField(max_length=256)
    location = models.CharField(null=True, max_length=256)
    photo = models.ImageField()

    class Meta():
        verbose_name_plural= "Criminals"