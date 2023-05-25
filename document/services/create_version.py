from document.models import Version


def create_version(document, sequence=None):
    """Create a new version for <document>"""

    return Version.objects.create(document=document, sequence=sequence or 1)


def create_next_version(document):
    """Create the next version for <document>"""

    last_version_sequence = document.get_latest_version().sequence
    return create_version(document, sequence=last_version_sequence + 1)
