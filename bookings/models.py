from django.db import models

class Repairman(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    location = models.CharField(max_length=255)  # Example location field
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    repairman = models.ForeignKey(Repairman, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)  # Customer's location from GPS
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Scheduled')

    def __str__(self):
        return f"Appointment with {self.repairman.name} on {self.date}"
