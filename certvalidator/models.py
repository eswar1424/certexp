from django.db import models

# Create your models here.

class Domain(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    hostname = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.hostname