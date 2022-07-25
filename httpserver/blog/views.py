from pydoc import doc
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, FileUpload, Document
from .forms import FileUploadForm
from . import models

from django.views.generic.detail import SingleObjectMixin
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage


# view 특 탬플릿으로 어떤거 보여줄지 결정함


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


# leupload.html', context)

def uploadFile(request):

    def getcontents(url):
        with open(str(document.uploadedFile.url()), encoding='utf-8') as txtfile:
            contents = ""
            for row in txtfile.readlines():
                contents = contents+row
        return contents

    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title=fileTitle,
            uploadedFile=uploadedFile,
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "blog/upload-file.html", context={
        "files": documents
    })
