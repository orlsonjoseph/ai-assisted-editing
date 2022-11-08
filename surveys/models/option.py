from django.db import models


class Option(models.Model):
    " An option for a question with a value and a description "

    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='options')
    order = models.IntegerField(default=0)

    value = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.value

    class Meta:
        index_together = ('question', 'order')
        ordering = ['id']
