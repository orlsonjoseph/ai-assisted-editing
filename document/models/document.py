from django.db import models
from django.contrib.auth import get_user_model

# from .folder import Folder

User = get_user_model()


class Document(models.Model):
    owner = models.ForeignKey(User, related_name="documents", on_delete=models.CASCADE)
    title = models.CharField(
        max_length=255, blank=False, null=False, default="Untitled Document"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-title", "-created_at"]

    def __str__(self):
        return f"<ID: {self.id}> by {self.owner}"

    def get_version(self, sequence):
        return self.versions.get(sequence=sequence)

    def get_latest_version(self):
        if hasattr(self, "versions") and self.versions.exists():
            return self.versions.order_by("-sequence").first()

        return None
