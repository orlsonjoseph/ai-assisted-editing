from document.models import Change


def create_change(snapshot, delta, state, sequence=None):
    """Create a new change for <snapshot.version.document> and <snapshot.version>"""

    new_change = Change(snapshot=snapshot, sequence=sequence or 1)
    new_change.operations = delta
    new_change.content = state

    return new_change.save()


def create_next_change(snapshot, delta, state):
    """Create the next change for <snapshot.version.document> and <snapshot.version>"""

    latest_change_sequence = snapshot.get_latest_change().sequence
    return create_change(snapshot, delta, state, sequence=latest_change_sequence + 1)
