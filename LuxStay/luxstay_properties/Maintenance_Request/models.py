from django.db import models

class MaintenanceRequest(models.Model):
    requestId = models.AutoField(primary_key=True)
    propertyId = models.IntegerField()
    requestDate = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Request {self.requestId} - {self.status}"