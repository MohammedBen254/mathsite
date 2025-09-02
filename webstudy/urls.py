from django.contrib import admin
from django.urls import path, include
# --- Add these two imports ---
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('', include('blog.urls')),
]

# --- Add this entire block at the end ---
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)