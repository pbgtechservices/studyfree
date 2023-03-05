from django.db import models
from datetime import date

# Create your models here.

class CollegeDataImage(models.Model):
    College_Image_Id = models.AutoField(primary_key=True)
    College_Image = models.FileField(max_length=1000)

    def __str__(self):
        return str(self.College_Image_Id)

class CollegeCategory(models.Model):
    College_Category = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.College_Category)

class CollegeDetailModel(models.Model):
    collegeName = models.CharField(max_length=254, null=False, blank=False)
    location = models.CharField(max_length=254, null=False, blank=False)
    rate = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    collegeType = models.CharField(max_length=254, null=False, blank=False)
    coursesOffered = models.CharField(max_length=254, null=False, blank=False)
    campusType = models.CharField(max_length=254, null=False, blank=False)
    examDate = models.DateField(default=date.today().strftime('%Y-%m-%d'))
    collegeImages = models.ManyToManyField(CollegeDataImage, related_name="college_images")
    address = models.CharField(max_length=254, null=False, blank=False)
    websiteLink = models.CharField(max_length=254, null=False, blank=False)
    contactNumber = models.CharField(max_length=254, null=False, blank=False)
    alteratePhoneNumber = models.CharField(max_length=254, null=False, blank=False)
    votes = models.IntegerField()
    linkName = models.CharField(max_length=254, null=True, blank=True)
    link = models.CharField(max_length=254, null=True, blank=True)
    linkButtonName = models.CharField(max_length=254, null=True, blank=True)
    youtubeUrls = models.JSONField(default=list, blank=True, null=True)
    category = models.ManyToManyField(CollegeCategory, related_name="college_category")
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return str(self.collegeName)

