from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    stars = models.DecimalField(max_digits=6, decimal_places=1, null=False, blank=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment {self.content} by {self.name}'
