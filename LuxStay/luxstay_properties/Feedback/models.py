from django.db import models

class Feedback(models.Model):
    feedbackId = models.AutoField(primary_key=True)
    propertyId = models.IntegerField()
    tenantId = models.IntegerField()
    submissionDate = models.DateField()
    starRating = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return f"Feedback {self.feedbackId} - {self.starRating} Stars"