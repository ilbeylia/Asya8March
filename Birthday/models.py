from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    selected_gif = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name