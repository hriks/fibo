# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from core.serializers import FibonacciSerializers, Fibonacci


class ListCreateFibonnaci(generics.ListCreateAPIView):
    queryset = Fibonacci.objects.all()
    serializer_class = FibonacciSerializers
