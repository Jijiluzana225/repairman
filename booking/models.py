from django.db import models

# Model for Repairman
class Repairman(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    location = models.CharField(max_length=255)  # Could be GPS coordinates in future

    def __str__(self):
        return f"{self.name} - {self.specialty}"

# Model for Booking
class Booking(models.Model):
    repairman = models.ForeignKey(Repairman, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    customer_location = models.CharField(max_length=255)  # Customer's GPS location
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.repairman.name} on {self.appointment_date}"
