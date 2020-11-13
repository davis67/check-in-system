from django.db import models
from core import models as core_models


class Visitor(core_models.TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Temperature(core_models.TimeStampedModel):
    value = models.CharField(max_length=100)
    visitor = models.ForeignKey("Visitor", on_delete=models.CASCADE)
    recorded_by = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True, limit_choices_to={'is_staff': True},)
