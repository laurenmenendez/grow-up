from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.child import Child
from .models.user import User

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '_all_'
