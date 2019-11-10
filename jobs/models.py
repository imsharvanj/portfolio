from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images', max_length=99)
    title = models.CharField(max_length=99, null=True, blank=True, default='')
    summary = models.CharField(max_length=199, null=True, blank=True, default='')

    def __str__(self):
        return self.title
