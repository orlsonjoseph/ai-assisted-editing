from django.contrib import admin

from document.models import Document, Snapshot, Version, Change

from .document import DocumentAdmin
from .snapshot import SnapshotAdmin
from .version import VersionAdmin
from .change import ChangeAdmin

admin.site.register(Document, DocumentAdmin)
admin.site.register(Snapshot, SnapshotAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(Change, ChangeAdmin)
