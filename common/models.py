from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class TimeStampedModel(models.Model):
    created_at = AutoCreatedField(db_index=True, verbose_name=('Criado em'))
    updated_at = AutoLastModifiedField(db_index=True, verbose_name=('Modificado em'))

    class Meta:
        abstract = True