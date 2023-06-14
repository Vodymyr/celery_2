from django.db import models


class SMSMessage(models.Model):
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    sent = models.BooleanField(default=False)


class Publication(models.Model):
    objects = None
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
