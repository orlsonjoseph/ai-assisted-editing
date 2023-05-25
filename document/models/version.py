from django.db import models


class Version(models.Model):
    document = models.ForeignKey(
        "Document", related_name="versions", on_delete=models.CASCADE
    )

    sequence = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("document", "sequence"),)
        ordering = ["document", "sequence"]

    def __str__(self):
        return f"Version {self.sequence} of {self.document}"

    def get_latest_snapshot(self):
        if hasattr(self, "snapshots") and self.snapshots.exists():
            return self.snapshots.order_by("-sequence").first()

        return None
