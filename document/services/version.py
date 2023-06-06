# Methods for the version model

from document.models import Version


class VersionService:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(VersionService, cls).__new__(cls)
        return cls.instance

    def create(self, document, sequence=None):
        return Version.objects.create(document=document, sequence=sequence or 1)

    def create_next(self, document):
        latest_sequence = document.get_latest_version().sequence
        return self.create(document, sequence=latest_sequence + 1)

    def get_or_create_latest(self, document):
        latest_version = document.get_latest_version()

        if not latest_version:
            return self.create(document)

        return latest_version
