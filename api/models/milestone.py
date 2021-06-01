from django.db import models
from django.contrib.auth import get_user_model
from .child import Child

class Milestone(models.Model):
  title = models.CharField(max_length=75)
  description = models.CharField(max_length=200)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  child = models.ForeignKey(
    Child,
    related_name = 'milestones',
    on_delete = models.CASCADE
  )

def __str__(self):
  # This must return a string
  return f"{self.title}: {self.description}"

def as_dict(self):
  """Returns dictionary version of Mango models"""
  return {
      'id': self.id,
      'title': self.title,
      'description': self.description
  }
