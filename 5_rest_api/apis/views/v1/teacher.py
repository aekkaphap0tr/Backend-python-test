from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Teacher
from apis.serializers import TeacherSerializer
from apis.filters import TeacherFilter

class TeacherAPI(ModelViewSet):
    queryall = Teacher.objects.all()
    serializers = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset= TeacherFilter
