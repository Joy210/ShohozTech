from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=3000, blank=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('posts:detail', kwargs={'id': self.id})
