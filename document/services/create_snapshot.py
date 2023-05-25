from document.models import Snapshot


def create_snapshot(version, sequence=None):
    """Create a new snapshot for <version.document> and <version>"""

    return Snapshot.objects.create(version=version, sequence=sequence or 1)


def create_next_snapshot(version):
    """Create the next snapshot for <version.document> and <version>"""

    latest_snapshot_sequence = document.get_latest_snapshot().sequence
    return create_snapshot(version, sequence=latest_snapshot_sequence + 1)
