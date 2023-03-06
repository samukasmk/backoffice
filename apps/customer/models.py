from django.db import models
from django.utils import timezone
from data.locations import cities, states, countries
from utils.django_models.field_choices import create_choices_tuple

client_types = ['individual', 'legal entity']


class Customer(models.Model):
    customer_type = models.CharField(max_length=30, choices=create_choices_tuple(client_types))
    name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=150, choices=[[city, city] for city in cities])
    state = models.CharField(max_length=150, choices=[[state, state] for state in states])
    country = models.CharField(max_length=150, choices=[[country, country] for country in countries])
    created_at = models.DateTimeField(default=timezone.now, editable=False, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, editable=False, blank=True)

    def __str__(self):
        return self.name
