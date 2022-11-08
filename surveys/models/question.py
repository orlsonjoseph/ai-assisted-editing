from django.db import models

QUESTION_TYPES = (
    (CHECKBOX := 'checkbox', 'Checkbox'),
    (COLOR := 'color', 'Color'),
    (COUNTRY := 'country', 'Country'),
    (DATE := 'date', 'Date'),
    (DATETIME := 'datetime', 'Datetime'),
    (EMAIL := 'email', 'Email'),
    (FILE := 'file', 'File'),
    (NUMBER := 'number', 'Number'),
    (RADIO := 'radio', 'Radio'),
    (RANGE := 'range', 'Range'),
    (SELECT := 'select', 'Select'),
    (TEL := 'tel', 'Telephone'),
    (TEXT := 'text', 'Text'),
    (TEXTAREA := 'textarea', 'Textarea'),
    (TIME := 'time', 'Time'),
    (URL := 'url', 'URL'),
)


class Question(models.Model):
    " A question with a prompt and a type "

    page = models.ForeignKey('Page', on_delete=models.CASCADE, related_name='questions')
    order = models.IntegerField(default=0)

    prompt = models.CharField(max_length=255)
    required = models.BooleanField(default=False)

    category = models.CharField(max_length=255, choices=QUESTION_TYPES, default=TEXT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        index_together = ('page', 'order')
        ordering = ['id']
