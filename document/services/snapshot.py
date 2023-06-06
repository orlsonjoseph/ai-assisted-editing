# Methods for the snapshot model

from document.models import Snapshot


class SnapshotService:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SnapshotService, cls).__new__(cls)
        return cls.instance

    def aggregate(self, snapshot):
        snapshot.version.content = snapshot.get_latest_change().content
        snapshot.version.save()

        snapshot.aggregated = True
        snapshot.save()

        snapshot.changes.order_by("sequence").all().delete()
        return snapshot

    def create(self, version, sequence=None):
        return Snapshot.objects.create(version=version, sequence=sequence or 1)

    def create_next(self, version):
        latest_sequence = version.get_latest_snapshot().sequence
        return self.create(version, sequence=latest_sequence + 1)

    def get_or_create_latest(self, version):
        latest_snapshot = version.get_latest_snapshot()

        if not latest_snapshot:
            return self.create(version)

        return latest_snapshot
