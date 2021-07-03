from rest_framework import mixins, viewsets

from .models import Key
from .serializers import KeySerializer


class KeyViewSet(
    mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    # API endpoint that allows creation of a new Key
    queryset = Key.objects.all()
    serializer_class = KeySerializer
