# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Fibonacci(models.Model):
    number = models.IntegerField()
    series = models.TextField(null=True, blank=True)
    runtime = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def fibonacci_series(self):
        return map(int, self.series.split(','))

    def calculate_fibonnaci_series(self):
        import timeit
        start = timeit.default_timer()
        fibs = [1, 1]
        for f in range(2, self.number):
            fibs.append(fibs[-1] + fibs[-2])
        self.runtime = timeit.default_timer() - start
        return "".join(map(str, fibs))
