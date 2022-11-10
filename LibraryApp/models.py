from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publication_date = models.DateField
    genre = models.CharField(max_length=150)
    featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='Unique_book')
        ]
    
    def __str__(self):
        return f"{self.title} by {self.author}"


