from django.db import models

from users.models import User


class File(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, null=True, blank=False)
    file = models.FileField(upload_to='uploads', blank=False, null=True)
    created_at = models.DateTimeField("Время создания", auto_now_add=True)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
    

    def __str__(self):
        return self.file.name
