from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1 import school,student,teacher

# In your urls.py
from rest_framework.routers import DefaultRouter
from apis.views.v1.school import SchoolAPI

router = DefaultRouter()
router.register(r'schools', SchoolAPI, basename='school')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
