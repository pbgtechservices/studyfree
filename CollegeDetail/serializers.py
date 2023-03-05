from rest_framework import fields, serializers

from CollegeDetail.models import CollegeDataImage, CollegeDetailModel


class College_Detail_Serializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Firm Details` instance, given the validated data.
        """
        return CollegeDetailModel.objects.create(**validated_data)

    class Meta:
        model = CollegeDetailModel
        fields = '__all__'
        depth = 2
        read_only_fields = ['id', 'collegeImages', 'category']    
        

class College_Image_Serializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Firm Details` instance, given the validated data.
        """
        return CollegeDataImage.objects.create(**validated_data)

    class Meta:
        model = CollegeDataImage
        fields = '__all__'
        # depth = 1