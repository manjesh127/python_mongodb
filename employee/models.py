from __future__ import unicode_literals
# name the import field of mongo model
from djongo import models


class Employee(models.Model):                      # collection name
    # auto update when data insert
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # auto update when data listen
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    # document
    name = models.CharField(max_length=25, null=True)
    age = models.IntegerField(default=10, null=True)
    employee_id = models.IntegerField(max_length=20, null=True)


def __str__(self):
    return self.name
