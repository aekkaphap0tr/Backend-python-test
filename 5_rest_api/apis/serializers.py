from rest_framework import serializers
from .models import School, Classroom, Teacher, Student


class SchoolSerializer(serializers.ModelSerializer):
    classroom_count = serializers.IntegerField(source='classrooms.count')
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'initials', 'address', 'classroom_count', 'teacher_count', 'student_count']

    def get_teacher_count(self, obj):
        return Teacher.objects.filter(classrooms__school=obj).distinct().count()

    def get_student_count(self, obj):
        return Student.objects.filter(classroom__school=obj).count()


class ClassroomSerializer(serializers.ModelSerializer):
    teachers = serializers.StringRelatedField(many=True)
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = Classroom
        fields = ['id', 'grade_level', 'group', 'school', 'teachers', 'students']


class TeacherSerializer(serializers.ModelSerializer):
    classrooms = serializers.StringRelatedField(many=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'surname', 'sex', 'classrooms']


class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'sex', 'classroom']
