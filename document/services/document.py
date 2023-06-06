# Methods for the Change model

from django.conf import settings

from document.models import Document

from .change import ChangeService
from .snapshot import SnapshotService
from .version import VersionService


class DocumentService:
    THRESHOLD = settings.AGGREGATION_THRESHOLD

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DocumentService, cls).__new__(cls)
        return cls.instance

    def create(self, owner):
        return Document.objects.create(owner=owner)

    def update(self, document, key, value):
        setattr(document, key, value)
        document.save()

        return document

    def update_title(self, document, value):
        return self.update(document, "title", value)

    def update_document(self, document, operations, content):
        version = VersionService().get_or_create_latest(document)
        snapshot = SnapshotService().get_or_create_latest(version)

        # IF the latest snapshot is aggregated, create a new snapshot
        if snapshot.aggregated:
            snapshot = SnapshotService().create_next(version)

        change = snapshot.get_latest_change()
        if not change:
            return ChangeService().create(snapshot, operations, content)

        # IF the sequence is less than the threshold, create the next change
        if change.sequence < self.THRESHOLD:
            return ChangeService().create_next(snapshot, operations, content)

        # IF the sequence is equal or greater to the threshold, aggregate the snapshot
        SnapshotService().aggregate(snapshot)

        latest_snapshot = SnapshotService().create_next(version)
        latest_change = ChangeService().create(latest_snapshot, operations, content)

        return latest_change
