"Course & Assignment serializers"

from rest_framework import serializers

from .models import Course, CourseAssignment

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"
        read_only = ("id",)


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseAssignment
        fields = "__all__"
        read_only = ("id", "updated")
