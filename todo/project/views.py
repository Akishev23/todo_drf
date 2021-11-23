from django.shortcuts import render
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from project.models import Project, ToDo
from project.serializers import ProjectSerializer, ToDoSerializer


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoModelViewSet(ModelViewSet):
    renderer_classes = [BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
