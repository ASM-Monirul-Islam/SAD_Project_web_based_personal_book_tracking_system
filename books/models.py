from django.db import models
from base.models import BaseModel
from django.utils.text import slugify



class Book(BaseModel):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, null=True, blank=True)
	author = models.CharField(max_length=255)
	publisher = models.CharField(max_length=255)
	publication_year = models.CharField(max_length=255)
	edition =  models.CharField(max_length=255)
	language = models.CharField(max_length=255)
	number_of_pages = models.IntegerField()
	description = models.TextField(blank=True, null=True)
	Genre = models.CharField(max_length=255)
	book_image = models.ImageField(upload_to='books', null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Book, self).save(*args, **kwargs)

	def __str__(self):
		return self.title
