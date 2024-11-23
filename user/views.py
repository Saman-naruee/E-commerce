from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer
from django.shortcuts import get_object_or_404
from .models import User, UserProfile

class UserProfileView(APIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_profile = get_object_or_404(UserProfile, user=user)
        serializer = self.serializer_class(user_profile)
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        serializer = self.serializer_class(user_profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request):
        user = request.user
        user_profile = get_object_or_404(UserProfile, user=user)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
