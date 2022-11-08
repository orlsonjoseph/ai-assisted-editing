from django.db import models


class Page(models.Model):
    " A page in a survey that contains questions "

    survey = models.ForeignKey('Survey', on_delete=models.CASCADE, related_name='pages')
    order = models.IntegerField(default=0)

    instructions = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        index_together = ('survey', 'order')
        ordering = ['id']
