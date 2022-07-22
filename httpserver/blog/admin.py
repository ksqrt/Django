from django.contrib import admin
from .models import Post, FileUpload, Document
from .models import FileUpload


admin.site.register(Post)
# admin.site.register(FileUpload)
admin.site.register(Document)
