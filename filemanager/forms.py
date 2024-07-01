from django import forms

from filemanager.models import UserFile


class UploadFileForm(forms.ModelForm):
    """Form definition for UploadFileForm."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = UserFile
        fields = ("file",)
        widgets = {
            "file": forms.FileInput(attrs={"accept": ".pdf"}),
        }

    file = forms.FileField()
