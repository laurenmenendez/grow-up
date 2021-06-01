from django.db import models
from django.contrib.auth import get_user_model

class Child(models.Model):
  name = models.CharField(max_length=75)
  age = models.IntegerField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

def __str__(self):
  # This must return a string
  return f"{self.name}, {self.age} years old."

def as_dict(self):
  """Returns dictionary version of Mango models"""
  return {
      'id': self.id,
      'name': self.name,
      'age': self.age
  }
