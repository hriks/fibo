from django.conf.urls import url
from core.views import ListCreateFibonnaci

urlpatterns = [
    url(r'^fibonnaci$', ListCreateFibonnaci),
]
