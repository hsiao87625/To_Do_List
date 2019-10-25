from django.db import models

# Create your models here.
class Mission(models.Model):
    mission = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.mission)