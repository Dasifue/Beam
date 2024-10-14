"REST API views"

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Course, CourseAssignment
from .serializers import CourseSerializer, AssignmentSerializer


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "pk"
    parser_classes = (MultiPartParser, FormParser)

class CourseAssignmentViewSet(viewsets.ModelViewSet):

    queryset = CourseAssignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field = "pk"
    parser_classes = (MultiPartParser, FormParser)
