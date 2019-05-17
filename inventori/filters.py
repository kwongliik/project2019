from django import forms
from django.contrib.auth.models import User, Group
from .models import Inventori
import django_filters

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')
    date_joined = django_filters.NumberFilter(lookup_expr='year',
        widget=forms.NumberInput(attrs={'placeholder': 'yyyy'}))
    #date_joined = django_filters.NumberFilter(lookup_expr='year__gt')
    #date_joined = django_filters.NumberFilter(lookup_expr='year__lt')
    groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'date_joined', 'groups']

        '''fields = {
            'username': ['exact', ],
            'first_name': ['icontains', ],
            'last_name': ['exact', ],
            'date_joined': ['year', 'year__gt', 'year__lt', ],
        }'''

class InventoriFilter(django_filters.FilterSet):
    inventori = django_filters.CharFilter(lookup_expr='icontains')
    created_by = django_filters.CharFilter(lookup_expr='username')
    #created_at = django_filters.DateFromToRangeFilter(lookup_expr='date')
    created_at = django_filters.DateFromToRangeFilter(lookup_expr='date',
        widget=django_filters.widgets.DateRangeWidget(attrs={'placeholder': 'mm/dd/yyyy'}))
    #updated_at = django_filters.DateFromToRangeFilter(lookup_expr='date')
    updated_at = django_filters.DateFromToRangeFilter(lookup_expr='date',
        widget=django_filters.widgets.DateRangeWidget(attrs={'placeholder': 'mm/dd/yyyy'}))

    class Meta:
        model = Inventori
        fields = ['id', 'inventori', 'harga', 'kuantiti',]