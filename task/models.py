from django.db import models
from django.contrib.auth.models import User

# User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_pics', blank=True)

    def _str_(self):
        return self.user.username


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    start_at = models.DateTimeField() 
    end_at = models.DateTimeField()
    thumbnail = models.CharField(max_length=150)

    def _str_(self):
        return self.title
    
    
# # User Group
class UserGroup(models.Model):
    name = models.CharField(max_length=100)
    members = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def _str_(self):
        return self.name
    
# Group
class Group(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

# Group Event
class GroupEvent(models.Model):
    group = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.title


# Interested Event
class InterestedEvent(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(GroupEvent, on_delete=models.CASCADE)


# Comment
class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.TextField()

    def _str_(self):
        return f"Comment by {self.user.username} on {self.event.title}"

# Image
class Image(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images')

    def _str_(self):
        return f"Image for {self.event.title}"