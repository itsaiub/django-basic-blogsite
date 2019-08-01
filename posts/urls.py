from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import redirect_view, post_list, post_details, post_create, post_update, post_delete

urlpatterns = [
    path('', redirect_view),
    path('posts/', post_list, name='posts'),
    path('posts/create', post_create),
    path('posts/<slug>/update', post_update),
    path('posts/<slug>/delete', post_delete),
    path('posts/<slug>', post_details),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
