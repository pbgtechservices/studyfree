from django.db import models

# Create your models here.
class CollegeCategoryModel(models.Model):
    college_category = models.JSONField(default=list, blank=True, null=True)