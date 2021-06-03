from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.milestone import Milestone
from ..serializers.milestone_serializer import MilestoneSerializer

# import json

# Create your views here.
class Milestones(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = MilestoneSerializer

    def get(self, request, child_pk):
        """Index request"""
        # Filter the milestones by child
        milestones = Milestone.objects.filter(child=child_pk)
        # Then filter these by child
        # Run the data through the serializer
        data = MilestoneSerializer(milestones, many=True).data
        return Response({ 'milestones': data })

    def post(self, request, child_pk):
        """Create request"""
        # Add user to request data object
        request.data['milestone']['owner'] = request.user.id
        request.data['milestone']['child'] = child_pk

        # data = json.loads(request.body)
        # Serialize/create mango
        milestone = MilestoneSerializer(data=request.data['milestone'])
        # If the child data is valid according to our serializer...
        if milestone.is_valid():
            # Save the created child & send a response
            milestone.save()
            return Response({ 'milestone': milestone.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(milestone.errors, status=status.HTTP_400_BAD_REQUEST)

class MilestoneDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        # Locate the milestone to show
        milestone = get_object_or_404(Milestone, pk=pk)
        # Only want to show owned milestones
        if not request.user.id == milestone.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this milestone')

        # Run the data through the serializer so it's formatted
        data = MilestoneSerializer(milestone).data
        return Response({ 'milestone': data })

    def delete(self, request, child_pk, pk):
        """Delete request"""
        # Locate child to delete
        milestone = get_object_or_404(Milestone, pk=pk)
        # Check the mango's owner agains the user making this request
        if not request.user.id == milestone.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this milestone')
        # Only delete if the user owns the  mango
        milestone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, child_pk, pk):
        """Update Request"""
        # Locate Mango
        # get_object_or_404 returns a object representation of our Mango
        milestone = get_object_or_404(Milestone, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == milestone.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this milestone')

        # Ensure the owner field is set to the current user's ID
        request.data['milestone']['owner'] = request.user.id
        request.data['milestone']['child'] = child_pk

        # Load request body as json
        # data = json.loads(request.body)
        # Validate updates with serializer
        milestone_data = MilestoneSerializer(milestone, data=request.data['milestone'], partial=True)
        if milestone_data.is_valid():
            # Save & send a 204 no content
            milestone_data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(milestone_data.errors, status=status.HTTP_400_BAD_REQUEST)
