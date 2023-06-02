from django.db import models

from delta import Delta
import json


class Change(models.Model):
    snapshot = models.ForeignKey(
        "Snapshot", related_name="changes", on_delete=models.CASCADE
    )

    sequence = models.PositiveIntegerField(default=1)

    operations = models.JSONField()
    content = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("snapshot", "sequence"),)
        ordering = ["snapshot", "sequence"]

    def __str__(self):
        return f"Change {self.sequence} of {self.snapshot}"

    def get_content(self):
        delta = Delta(self.content["ops"]).compose(Delta(self.operations["ops"]))

        to_serialize = f"'ops': {delta.ops}"
        to_serialize = "{" + to_serialize + "}"

        return to_serialize
