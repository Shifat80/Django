from django.db import models

# Create your models here.
class TourAsia(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(("Price"), max_digits=5, decimal_places=2)

    def __str__(self):
        return f"ID:{self.id} from {self.origin} to {self.destination} date {self.date} time {self.time} price {self.price}"