from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import School
from apis.serializers import SchoolSerializer
from apis.filters import SchoolFilter

class SchoolAPI(ModelViewSet):
    queryall = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter