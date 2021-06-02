from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.child import Child
from ..serializers.child_serializer import ChildSerializer

# import json

# Create your views here.
class Children(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ChildSerializer
    def get(self, request):
        """Index request"""
        # Get all the children:
        # Filter the children by owner, so you can only see your owned children
        children = Child.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ChildSerializer(children, many=True).data
        return Response({ 'children': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['child']['owner'] = request.user.id

        # data = json.loads(request.body)
        # Serialize/create mango
        child = ChildSerializer(data=request.data['child'])
        # If the child data is valid according to our serializer...
        if child.is_valid():
            # Save the created child & send a response
            child.save()
            return Response({ 'child': child.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(child.errors, status=status.HTTP_400_BAD_REQUEST)

class ChildDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the child to show
        child = get_object_or_404(Child, pk=pk)
        # Only want to show owned children
        if not request.user.id == child.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this child')

        # Run the data through the serializer so it's formatted
        data = ChildSerializer(child).data
        return Response({ 'child': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate child to delete
        child = get_object_or_404(Child, pk=pk)
        # Check the mango's owner agains the user making this request
        if not request.user.id == child.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this child')
        # Only delete if the user owns the  mango
        child.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Mango
        # get_object_or_404 returns a object representation of our Mango
        child = get_object_or_404(Child, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == child.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this child')

        # Ensure the owner field is set to the current user's ID
        request.data['child']['owner'] = request.user.id
        # Validate updates with serializer
        data = ChildSerializer(child, data=request.data['child'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
