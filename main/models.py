from django.db import models

# Create your models here.
class MASEntry(models.Model):
	mas_entry_date = models.DateTimeField('date entry')
	mas_entry_item = models.TextField()
	
	# To do : convert it to number field
	mas_entry_quantity = models.CharField(max_length=200)
	
	mas_entry_location = models.TextField()
	mas_entry_remarks = models.TextField()

	def __str__(self):
		return f"{self.mas_entry_date} : " + self.mas_entry_item
		
		