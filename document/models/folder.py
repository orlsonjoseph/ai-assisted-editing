from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Folder(models.Model):
    owner = models.ForeignKey(User, related_name="folders", on_delete=models.CASCADE)
    title = models.CharField(
        max_length=255, blank=False, null=False, default="Untitled Folder"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return f"{self.title} by {self.owner}"

    def get_documents(self):
        return self.documents.all()
