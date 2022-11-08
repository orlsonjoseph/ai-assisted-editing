from django.db import models
from django.urls import reverse
from django.conf import settings


class Survey(models.Model):
    " A survey that contains pages "

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, related_name='surveys')

    title = models.CharField(max_length=255)
    description = models.TextField()

    is_published = models.BooleanField(default=False)

    published_at = models.DateTimeField(default=None, null=True)
    expiring_at = models.DateTimeField(default=None, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    redirect_url = models.URLField(default=None, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']

    @property
    def safe_name(self):
        return self.title.replace(' ', '_').encode('utf-8').decode('ascii', 'ignore')

    def get_absolute_url(self):
        return reverse('surveys:show', kwargs={'pk': self.pk})
