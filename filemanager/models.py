from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class UserFile(models.Model):
    filename = models.FileField(
        upload_to="user_files",
        validators=[FileExtensionValidator(["pdf", "png", "jpg"])],
    )

    def __str__(self) -> str:
        return self.filename
