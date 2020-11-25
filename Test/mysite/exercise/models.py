from django.db import models


class InputModel(models.Model):
    input_field = models.CharField(max_length=30)
    data = models.JSONField()

    def __str__(self):
        return self.data, self.input_field
