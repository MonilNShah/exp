from django.db import models
import uuid 
import datetime

# Create your models here.
class book(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
	book_name=models.CharField(max_length=25)
	Author_name=models.CharField(max_length=30)
	# date=models.DateField(default=date())
	date = models.DateField(default=datetime.date.today)

	def __str__(self):
		return (self.book_name)