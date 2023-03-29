from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from config import settings

favicon_view = RedirectView.as_view(url='/static/core/media/logo/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', favicon_view),
]

if settings.base.DEBUG:
    urlpatterns += static(settings.base.STATIC_URL, document_root=settings.base.STATIC_ROOT)
    urlpatterns += static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)
