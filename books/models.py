from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
from django.contrib.auth.models import User

class Genre(BaseModel):
	genre = models.CharField(max_length=100)
	slug = models.SlugField(unique=True, null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.genre)
		super(Genre, self).save(*args, **kwargs)

	def __str__(self):
		return self.genre

class Book(BaseModel):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, null=True, blank=True)
	author = models.CharField(max_length=255)
	publication_year = models.CharField(max_length=255)
	language = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
	book_image = models.ImageField(upload_to='books/', null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Book, self).save(*args, **kwargs)

	def __str__(self):
		return self.title


