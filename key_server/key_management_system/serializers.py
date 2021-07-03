from rest_framework import serializers

from .models import Key


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ["key_ref", "key", "init_vector", "expire_date", "created"]
