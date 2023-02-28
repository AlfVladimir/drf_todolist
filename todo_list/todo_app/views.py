from rest_framework import viewsets, mixins
from todo_app.models import Tasklist

from rest_framework import filters
from .serializers import TasklistSerializer
from .filters import TasklistFilterSet


class TasklistViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Tasklist.objects.all().order_by("-id")
    serializer_class = TasklistSerializer

    ordering_fields = ["text", "is_done", "timestamp_create", "timestamp_done"]
    filterset_fields = ["text", "is_done"]
    filterset_class = TasklistFilterSet
