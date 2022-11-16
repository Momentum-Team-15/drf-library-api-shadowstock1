from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

GENRES ={
    ('Fantasy','Fantasy'),
    ('Nonfiction', 'Nonfiction'),
    ('Sci-Fi','Sci-Fi'),
    ('Thriller','Thriller'),
    ('Mystery', 'Mystery'),
    ('History','History'),
    ('Kids','Kids'),
    ('Fiction','Fiction')
}
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50,default='Nonfiction',choices=GENRES)
    featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='Unique_book')
        ]
    
    def __str__(self):
        return f"{self.title} by {self.author}"

STATUS_CHOICES = {
    ('Reading', 'Reading'),
    ('Want-to-read','Want-to-read'),
    ('Read/Done', 'Read/Done'),
    ('No Status', 'No Status'),
}

class Tracker(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=50, default='No Status', choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.status}"

SHARED = {
    ('Public','Public'),
    ('Private','Private')
}
class Note(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE,blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length=4000, blank=True, null=True)
    private = models.CharField(max_length=20, default='Private', choices=SHARED)

    def __str__(self):
        return f"{self.book} notes created at {self.created_at}"
    




