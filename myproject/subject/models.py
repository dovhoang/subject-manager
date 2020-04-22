from django.db import models


# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=200)


class TypeSub(models.Model):
    type_id = models.BooleanField(primary_key=True)
    type_name = models.CharField(max_length=100)


class Subject(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(TypeSub, on_delete=models.CASCADE)
    tc = models.IntegerField(default=2)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
