import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_set = models.ManyToManyField('RoomType', blank=True)
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.FloatField(default=0, blank=True)
    statusStartDate = models.DateField(null=True)
    statusEndDate = models.DateField(null=True)

    def __str__(self):
        return f'id : {self.id}'


class RoomType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(blank=True, upload_to='%Y/%m')


class Comment(models.Model):
    post_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'rating :{self.rating} body :{self.body}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        rating_avg = Comment.objects.filter(post_id=self.post_id).aggregate(Avg('rating'))
        Room.objects.filter(id=self.post_id.id).update(rating=rating_avg['rating__avg'])
