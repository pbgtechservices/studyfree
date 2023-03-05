from django.db import models

# Create your models here.
class StudentDetailModel(models.Model):
    studentName = models.CharField(max_length=254, null=False, blank=False)
    fatherName = models.CharField(max_length=254, null=False, blank=False)
    presentSchoolName = models.CharField(max_length=254, null=False, blank=False)
    district = models.CharField(max_length=254, null=False, blank=False)
    expectedResultInTenth = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return str(self.studentName)