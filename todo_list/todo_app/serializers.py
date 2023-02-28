from rest_framework import serializers
from todo_app.models import Tasklist


class TasklistSerializer(serializers.ModelSerializer):
    """Сериализатор по модели Tasklist"""

    class Meta:
        model = Tasklist
        fields = "__all__"
