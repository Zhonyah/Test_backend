from rest_framework import viewsets, routers
from .models import Personnel, SchoolStructure, Schools, Classes, Subjects, StudentSubjectsScore
from .serializer import PersonnelSerializer, SchoolStructureSerializer, SchoolSerializer, ClassesSerializer, SubjectsSerializer, StudentSubjectsScoreSerializer


class PersonnelApiViews (viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer


class SchoolStructureApiViews (viewsets.ModelViewSet):
    queryset = SchoolStructure.objects.all()
    serializer_class = SchoolStructureSerializer


class SchoolApiViews (viewsets.ModelViewSet):
    queryset = Schools.objects.all()
    serializer_class = SchoolSerializer


class ClassesApiViews (viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer


class SubjectsApiViews (viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer


class StudentSubjectsScoreApiViews (viewsets.ModelViewSet):
    queryset = StudentSubjectsScore.objects.all()
    serializer_class = StudentSubjectsScoreSerializer


routers = routers.DefaultRouter()
routers.register(r'Personnel', PersonnelApiViews)
routers.register(r'SchoolStructure', SchoolStructureApiViews)
routers.register(r'School', SchoolApiViews)
routers.register(r'Classess', ClassesApiViews)
routers.register(r'Subjectss', SubjectsApiViews)
routers.register(r'StudentSubjectsScore', StudentSubjectsScoreApiViews)
