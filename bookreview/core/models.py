from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to="cover")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
