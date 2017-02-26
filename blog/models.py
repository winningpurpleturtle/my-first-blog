from django.db import models
from django.utils import timezone

class Post(models.Model):
	yazar = models.ForeignKey("auth.User")
	baslik = models.CharField(max_length=200)
	yazi = models.TextField()
	yaratilma_tarihi = models.DateTimeField(blank=True, null=True)

	def yayinla(self):
		self.yayinlanma_tarihi= timeone.now()
		self.save()

	def __str__(self):
	    return self.baslik
