from django.contrib.auth.models import User

from django.forms import CheckboxSelectMultiple
import django_filters

from .models import Course, Result

class Filter_Course(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    author = django_filters.ModelMultipleChoiceFilter(
        queryset = User.objects.all(),
        widget = CheckboxSelectMultiple(),
        label = ' Author: ',
    )
    start_date = django_filters.DateFilter(field_name='date_Created', lookup_expr='gte')
    stop_date = django_filters.DateFilter(field_name='date_Created', lookup_expr='lte')
    Des_contains = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    class Meta:
        model = Course
        fields = []


class Filter_Result(django_filters.FilterSet):
    module = django_filters.CharFilter(field_name='module.name', lookup_expr='icontains')
    start_date = django_filters.DateFilter(field_name='time', lookup_expr='gte')
    stop_date = django_filters.DateFilter(field_name='time', lookup_expr='lte')
    class Meta:
        model = Result
        fields = [] 