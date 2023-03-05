from rest_framework import fields, serializers
from CollegeCategory.models import CollegeCategoryModel


class College_Category_Serializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Firm Details` instance, given the validated data.
        """
        return CollegeCategoryModel.objects.create(**validated_data)

    class Meta:
        model = CollegeCategoryModel
        fields = '__all__'  