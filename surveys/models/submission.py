from django.db import models


class Submission(models.Model):
    " A submission to a survey "

    survey = models.ForeignKey('Survey', on_delete=models.CASCADE, related_name='submissions')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['id']
