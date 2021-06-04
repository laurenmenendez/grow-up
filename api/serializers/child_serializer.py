from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models.child import Child
from ..models.user import User

class ChildSerializer(serializers.ModelSerializer):

    # creates an array of milestone objects on the user instance
    milestones = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Child
        fields = '__all__'
