from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Student
from apis.serializers import StudentSerializer
from apis.filters import StudentFilter

class StudentAPI(ModelViewSet):
    queryall = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter
