from django.db import models


# Create your models here.
class Room(models.Model):
    room_categories = (
        ("AC", "AC"),
        ("NON-AC", "NON-AC"),
        ("DEL", "DELUXE"),
        ("KING", "KING"),
        ("QUEEN", "QUEEN")
    )
    number = models.IntegerField()
    category = models.CharField(max_length=20, choices=room_categories)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds}beds for {self.capacity} people'
