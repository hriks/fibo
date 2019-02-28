from rest_framework import serializers

from core.models import Fibonacci


class FibonacciSerializers(serializers.ModelSerializer):

    class Meta:
        model = Fibonacci
        fields = ('number', 'series', 'runtime', 'created')
