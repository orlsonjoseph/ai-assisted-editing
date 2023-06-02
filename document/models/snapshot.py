from django.db import models

# TODO move threshold
from django.conf import settings

THRESHOLD = settings.AGGREGATION_THRESHOLD


class Snapshot(models.Model):
    version = models.ForeignKey(
        "Version", related_name="snapshots", on_delete=models.CASCADE
    )

    sequence = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    aggregated = models.BooleanField(default=False)

    class Meta:
        unique_together = (("version", "sequence"),)
        ordering = ["version", "sequence", "-created_at"]

    def __str__(self):
        return f"Snapshot {self.sequence} of {self.version}"

    # TODO: Once a snapshot has reached the threshold, it will be aggregated
    # An aggregated snapshot will be frozen and will not be updated
    # def save(self, override=False, *args, **kwargs):
    #     if not self.aggregated or override:
    #         super(Snapshot, self).save(*args, **kwargs)

    def get_latest_change(self):
        if hasattr(self, "changes") and self.changes.exists():
            return self.changes.order_by("-sequence").first()

        return None

    def get_content(self):
        latest_change = self.get_latest_change()
        return latest_change.get_content() if latest_change else None
