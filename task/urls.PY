from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileVieSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileVieSet)

urlpatterns = [
    path('', include(router.urls))
]
