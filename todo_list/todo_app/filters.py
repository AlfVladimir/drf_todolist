from django_filters import rest_framework as dj_filters
from .models import Tasklist


class TasklistFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели статей."""

    text = dj_filters.CharFilter(field_name="text", lookup_expr="icontains")
    is_done = dj_filters.BooleanFilter(field_name="is_done")

    # order_by_field = "ordering"
    # order_by_field = ['text', 'is_done', 'timestamp_create', 'timestamp_done']

    class Meta:
        model = Tasklist
        fields = ["text", "is_done"]
