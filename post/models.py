from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields
# Create your models here.


class summer_note_model(summer_model.Attachment):
    summer_field = summer_fields.SummernoteTextField()