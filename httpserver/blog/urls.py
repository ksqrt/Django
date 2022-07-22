from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('fileupload/', views.fileUpload, name="fileupload"),
    path("", views.uploadFile, name="upload-file"),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
