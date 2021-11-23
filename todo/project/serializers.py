from rest_framework.serializers import HyperlinkedModelSerializer, MultipleChoiceField

from users.serializers import UserModelSerializer
from .models import Project, ToDo
from users.models import Users


class ProjectSerializer(HyperlinkedModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
