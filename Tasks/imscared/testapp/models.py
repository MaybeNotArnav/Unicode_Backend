from django.db import models


class apis(models.Model):
    userid = models.CharField(max_length=122, default=96479162)
    username = models.CharField(max_length=40, blank=True, null=True)
    no = models.PositiveSmallIntegerField(max_length=50)

    def __str__(self):
        return self.username
