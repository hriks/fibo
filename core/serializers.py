import pytz
from rest_framework import serializers

from core.models import Fibonacci


class FibonacciSerializers(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()

    def get_created(self, obj):
        return obj.created.astimezone(
            pytz.timezone("Asia/Kolkata")).strftime("%d %b %Y %k:%M %p")

    class Meta:
        model = Fibonacci
        fields = ('number', 'fibonacci_series', 'runtime', 'created')
        read_only_fields = ('created', 'runtime')
