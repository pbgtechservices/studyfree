from rest_framework import fields, serializers

from StudentData.models import StudentDetailModel


class Student_Detail_Serializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Firm Details` instance, given the validated data.
        """
        return StudentDetailModel.objects.create(**validated_data)

    class Meta:
        model = StudentDetailModel
        fields = '__all__'
        # depth = 2
        read_only_fields = ['id']    
        