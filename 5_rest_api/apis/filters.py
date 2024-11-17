from django_filters import FilterSet, filters
import django_filters
from .models import School, Classroom, Teacher, Student


class SchoolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']


class ClassroomFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(field_name='school__id')

    class Meta:
        model = Classroom
        fields = ['school']


class TeacherFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(field_name='classrooms__school__id')
    classroom = django_filters.NumberFilter(field_name='classrooms__id')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    surname = django_filters.CharFilter(field_name='surname', lookup_expr='icontains')
    sex = django_filters.ChoiceFilter(choices=Teacher.gender)

    class Meta:
        model = Teacher
        fields = ['school', 'classroom', 'name', 'surname', 'sex']


class StudentFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(field_name='classroom__school__id')
    classroom = django_filters.NumberFilter(field_name='classroom__id')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    surname = django_filters.CharFilter(field_name='surname', lookup_expr='icontains')
    sex = django_filters.ChoiceFilter(choices=Student.gender)

    class Meta:
        model = Student
        fields = ['school', 'classroom', 'name', 'surname', 'sex']
