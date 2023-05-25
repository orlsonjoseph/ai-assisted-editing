from django.db import models


class Change(models.Model):
    snapshot = models.ForeignKey(
        "Snapshot", related_name="changes", on_delete=models.CASCADE
    )

    sequence = models.PositiveIntegerField(default=1)

    operations = models.JSONField()
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("snapshot", "sequence"),)
        ordering = ["snapshot", "sequence"]

    def __str__(self):
        return f"Change {self.sequence} of {self.snapshot}"
