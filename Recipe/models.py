from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Recipe(models.Model):
    
    title = models.CharField(max_length=150)
    image = models.ImageField()
    ingredients = models.TextField()
    instructions = models.TextField()
    video = EmbedVideoField(default='')

    class Meta:
        abstract = True  # Making this an abstract base class

    def __str__(self):
        return self.title

class breakfast_details(Recipe):
    pass

class dinner_details(Recipe):
    pass

class juice_details(Recipe):
    pass

class lunch_details(Recipe):
    pass

class sweet_details(Recipe):
    pass
