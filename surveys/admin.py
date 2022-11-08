from django.contrib import admin

from .models import Answer, Option, Page, Question, Survey, Submission
# Register your models here.

admin.site.register(Answer)
admin.site.register(Option)
admin.site.register(Page)
admin.site.register(Question)
admin.site.register(Survey)
admin.site.register(Submission)
