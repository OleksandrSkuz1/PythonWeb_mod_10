from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biography = models.TextField(blank=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

