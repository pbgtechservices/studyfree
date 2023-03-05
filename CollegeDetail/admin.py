from django.contrib import admin

from CollegeDetail.models import CollegeCategory, CollegeDataImage, CollegeDetailModel

# Register your models here.
admin.site.register(CollegeDetailModel)
admin.site.register(CollegeCategory)
admin.site.register(CollegeDataImage)