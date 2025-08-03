from django.contrib import admin
from django.urls import path, include

# ✅ Import these for media file handling
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # include app-level urls
]

# ✅ Add this at the bottom (outside the list!)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
