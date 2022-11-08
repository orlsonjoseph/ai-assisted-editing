from django.db import models


class Answer(models.Model):
    " An answer to a question with either a value or a reference to an option "

    submission = models.ForeignKey('Submission', on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')

    option = models.ForeignKey('Option', on_delete=models.CASCADE,
                               related_name='answers', null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.value

    class Meta:
        ordering = ['id']
