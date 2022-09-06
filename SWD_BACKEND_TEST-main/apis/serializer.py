from rest_framework import serializers
from .models import Personnel, SchoolStructure, Schools, Classes, Subjects, StudentSubjectsScore


class SchoolStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolStructure
        fields = ('title', 'parent')


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ('first_name', 'last_name', 'school_class', 'personnel_type')
        


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ('school', 'class_order')


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = "__all__"


class StudentSubjectsScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubjectsScore
        fields = ('student', 'subjects', 'credit', 'score')
