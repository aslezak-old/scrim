from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=200)
    prefix = models.CharField(max_length=4)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='/media', blank=True, null=True)
    wins = models.IntegerField(default=0, null=True)
    loses = models.IntegerField(default=0, null=True)

    LEAGUE_CHOICES = (
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
        ('P', 'Platinum'),
        ('D', 'Diamond'),
        ('C', 'Challenger'),
    )

    league = models.CharField(max_length=1, choices=LEAGUE_CHOICES, null=True, blank=True)

    def __unicode__(self):
        return self.name
