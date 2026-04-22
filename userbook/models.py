from django.db import models
from base.models import BaseModel
from books.models import Book
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class UserBook(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    STATUS_CHOICES = [
        ('Wishlist', 'Wishlist'),
        ('Reading', 'Reading'),
        ('Completed', 'Completed'),
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Wishlist")
    
    rating = models.IntegerField(
		validators=[MinValueValidator(1), MaxValueValidator(5)],
		null=True,
		blank=True,
        default=None
	)
    
    comments = models.TextField(null=True, blank=True)
    
    wishlist = models.BooleanField(default=True)
    reading = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}-{self.book.title}"
    
    class Meta:
    	unique_together = ['user', 'book']