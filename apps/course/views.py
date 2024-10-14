"REST API views"

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Course, CourseAssignment
from .serializers import CourseSerializer, AssignmentSerializer


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "pk"
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        product = serializer.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "course_creates",
            {
                "type": "course.created",
                "message": f"Course '{product.name}' has been created.",
            },
        )

class CourseAssignmentViewSet(viewsets.ModelViewSet):

    queryset = CourseAssignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field = "pk"
    parser_classes = (MultiPartParser, FormParser)
