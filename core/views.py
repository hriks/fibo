# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import View

from rest_framework import generics, permissions

from core.serializers import FibonacciSerializers, Fibonacci


class FibonacciView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ListCreateFibonnaci(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Fibonacci.objects.all()
    serializer_class = FibonacciSerializers
