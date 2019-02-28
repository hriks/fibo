from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from fibo.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls')),
] + static(
    MEDIA_URL, document_root=MEDIA_ROOT
)
