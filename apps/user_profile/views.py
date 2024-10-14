"REST API views"

from rest_framework import viewsets, mixins
from rest_framework.parsers import MultiPartParser, FormParser

from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer, UserCreateSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
    parser_classes = (MultiPartParser, FormParser)

class UserCreateViewSet(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    lookup_field = "pk"
    parser_classes = (MultiPartParser, FormParser)

class UserProfileViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "pk"
    parser_classes = (MultiPartParser, FormParser)
