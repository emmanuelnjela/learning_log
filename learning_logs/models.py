from django.db import models

# Create your models here.
class Topic(models.Model):
    """Creating Model Topic"""
    text = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the string representation of the model"""
        return self.text

class Entry(models.Model):
    """Creating Model Entry"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return the string representation of the model"""
        return f"{self.text[:50]}..."
    