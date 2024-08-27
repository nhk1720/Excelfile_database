from rest_framework import serializers
from .models import Student



# class Student_serializer(serializers.Serializer):
#     class Meta:
#         model=Student
#         fields=('name','age','city')


class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        return Student.objects.create(**validated_data)