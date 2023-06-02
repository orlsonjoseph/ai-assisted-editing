def aggregate_snapshot(snapshot):
    # Retrieve the list of changes for the snapshot
    set_of_changes = snapshot.changes.order_by("sequence").all()

    snapshot.version.content = snapshot.get_latest_change().content
    snapshot.version.save()

    snapshot.aggregated = True
    snapshot.save()

    set_of_changes.delete()
    return snapshot
