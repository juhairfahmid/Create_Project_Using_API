from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    