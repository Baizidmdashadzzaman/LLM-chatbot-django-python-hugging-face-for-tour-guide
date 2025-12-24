from django.contrib import admin
from django.urls import path, include
from . import views
from . import ai_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ai-chat/', ai_views.ai_chat_proxy, name='ai_chat_proxy')
]

# Serve media and static files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
