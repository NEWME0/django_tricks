from django.db.models import *


class CreatedUpdatedAt(Model):
    created_at = DateTimeField(editable=False, auto_now_add=True)
    updated_at = DateTimeField(editable=False, auto_now=True)

    class Meta:
        abstract = True
