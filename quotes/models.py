from django.db import models


class Quote(models.Model):

    quote_author = models.CharField(max_length=60)
    quote_body = models.TextField()
    context = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100,  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quote_author}: {self.quote_body[:40]}..."
