# Methods for the Change model

from document.models import Change


class ChangeService:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ChangeService, cls).__new__(cls)
        return cls.instance

    def create(self, snapshot, operations, content, sequence=None):
        return Change.objects.create(
            snapshot=snapshot,
            sequence=sequence or 1,
            operations=operations,
            content=content,
        )

    def create_next(self, snapshot, operations, content):
        latest_sequence = snapshot.get_latest_change().sequence
        return self.create(snapshot, operations, content, sequence=latest_sequence + 1)
