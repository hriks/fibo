from django.conf.urls import url
from core.views import ListCreateFibonnaci, FibonacciView

urlpatterns = [
    url(r'^api/fibonnaci$', ListCreateFibonnaci.as_view()),
    url(r'^', FibonacciView.as_view()),
]
