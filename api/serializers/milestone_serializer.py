from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models.milestone import Milestone
from ..models.user import User

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'
