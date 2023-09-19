from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer, UserProfileImageUpdateSerializer

# Create your views here.


class UserProfileVieSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
    
    # For update avatar
    @action(detail=True, methods=['PUT'], serializer_class=UserProfileImageUpdateSerializer)
    def update_profile_image(self, request, pk=None):
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)