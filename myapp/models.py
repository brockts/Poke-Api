from django.db import models

class Test(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)