from django.db.models import *

from ..abstract.models import CreatedUpdatedAt


class Scope(CreatedUpdatedAt, Model):
    title = CharField(max_length=127)

    def __str__(self):
        return f'{self.pk} - {self.title}'

    class Meta:
        db_table = 'scopes'


class Role(CreatedUpdatedAt, Model):
    title = CharField(max_length=127)
    scopes = ManyToManyField(Scope)

    def __str__(self):
        return f'{self.pk} - {self.title}'

    class Meta:
        db_table = 'roles'
