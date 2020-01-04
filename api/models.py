from django.db import models


class APIInfo(models.Model):
    api_name = models.CharField(max_length=32)
