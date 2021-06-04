from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.milestone import Milestone
from ..serializers.milestone_serializer import MilestoneSerializer

# Create your views here.
class Milestones(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = MilestoneSerializer

    def get(self, request, child_pk):
        """Index request"""
        # Filter the milestones by child, only want to see milestones for specific child
        milestones = Milestone.objects.filter(child=child_pk)
        # Run the data through the serializer
        data = MilestoneSerializer(milestones, many=True).data
        return Response({ 'milestones': data })

    def post(self, request, child_pk):
        """Create request"""
        # Add user to request data object
        request.data['milestone']['owner'] = request.user.id
        # Add child to request data object - allows this milestone to be searchable by child later
        request.data['milestone']['child'] = child_pk

        # Serialize/create milestone
        milestone = MilestoneSerializer(data=request.data['milestone'])
        # If the milestone data is valid according to our serializer...
        if milestone.is_valid():
            # Save the created milestone & send a response
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
        # Locate milestone to delete
        milestone = get_object_or_404(Milestone, pk=pk)
        # Check the milestone's owner agains the user making this request
        if not request.user.id == milestone.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this milestone')
        # Only delete if the user owns the milestone
        milestone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, child_pk, pk):
        """Update Request"""
        # Locate milestone
        # get_object_or_404 returns a object representation of our milestone
        milestone = get_object_or_404(Milestone, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == milestone.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this milestone')

        # Ensure the owner field is set to the current user's ID
        request.data['milestone']['owner'] = request.user.id
        # ensure child field is set to current child
        request.data['milestone']['child'] = child_pk

        # Validate updates with serializer
        milestone_data = MilestoneSerializer(milestone, data=request.data['milestone'], partial=True)
        if milestone_data.is_valid():
            # Save & send a 204 no content
            milestone_data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(milestone_data.errors, status=status.HTTP_400_BAD_REQUEST)
