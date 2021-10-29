from django.db import models

# Create your models here.
class Poll(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title
