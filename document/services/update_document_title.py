from document.models import Document


def update_document_title(document, new_title):
    """Update the title of <document> to <new_title>"""

    document.title = new_title
    document.save()

    return document
