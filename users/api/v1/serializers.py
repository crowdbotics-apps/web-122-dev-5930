from rest_framework import serializers
from users.models import Ggjyu


class GgjyuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ggjyu
        fields = "__all__"
