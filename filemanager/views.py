from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import UploadFileForm
from .models import UserFile

# Create your views here


class UploadFile(CreateView):
    template_name = "filemanager/upload_file.html"
    model = UserFile
    fields = "__all__"
    success_url = "/filemanager"


class ListFiles(ListView):
    model = UserFile
    template_name = "filemanager/list_files.html"
    context_object_name = "files"
