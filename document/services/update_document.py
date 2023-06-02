from django.conf import settings

from .create_version import create_version, create_next_version
from .create_snapshot import create_snapshot, create_next_snapshot
from .create_change import create_change, create_next_change

from .aggregate_snapshot import aggregate_snapshot

THRESHOLD = settings.AGGREGATION_THRESHOLD


def update_document(document, operations, content):
    latest_version = document.get_latest_version() or create_version(document)
    latest_snapshot = latest_version.get_latest_snapshot() or create_snapshot(
        latest_version
    )

    # IF the latest snapshot is aggregated, create a new snapshot
    if latest_snapshot.aggregated:
        latest_snapshot = create_next_snapshot(latest_version)

    latest_change = latest_snapshot.get_latest_change()
    if not latest_change:
        return create_change(latest_snapshot, operations, content)

    # IF the sequence is less than the threshold, create the next change
    if latest_change.sequence < THRESHOLD:
        return create_next_change(latest_snapshot, operations, content)

    # IF the sequence is equal or greater to the threshold, aggregate the snapshot
    aggregate_snapshot(latest_snapshot)

    latest_snapshot = create_next_snapshot(latest_version)
    return create_change(latest_snapshot, operations, content)
