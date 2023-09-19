from rest_framework import serializers
from .models import UserProfile, UserGroup, Group, GroupEvent, InterestedEvent, Event, Comment, Image


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = '__all__'
        
        
class  UserProfileImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['image']
        
        
class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'
        

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
        
class GroupEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupEvent
        fields = '__all__'
        
        
class InterestedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestedEvent
        fields = '__all__'
        
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'