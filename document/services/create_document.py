from document.models import Document, Version


def create_document(owner):
    """Create a new document for <owner>"""

    document = Document.objects.create(owner=owner)
    return document
