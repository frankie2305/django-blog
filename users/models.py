from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default='default.jpg', upload_to='thumbnails')

    def __str__(self):
        return f"{self.user.username}'s profile"

    def save(self):
        super().save()

        image = Image.open(self.thumbnail.path)

        # resize image
        output_size = (125, 125)
        image.thumbnail(output_size)
        image.save(self.thumbnail.path)
