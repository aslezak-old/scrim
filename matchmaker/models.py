from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=200)
    prefix = models.CharField(max_length=4)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='/media', blank=True, null=True)

    def __unicode__(self):
        return self.name