from django.conf import settings
from django.db import models

# Create your models here.

#class User(models.Model):
#	name = models.CharField(max_length = 200)
#	email = models.EmailField(max_length = 254)
#	password = models.CharField(max_length = 200)
#	def __unicode__(self):
#		return self.name

class WishList(models.Model):
	title = models.CharField(max_length = 200)
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='wishlist_creator')
	viewers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wishlist_viewer')
	def __unicode__(self):
		return self.title

class Gift(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField(null=True, blank=True)
	image = models.CharField(max_length = 200, null=True, blank=True)
	wisher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='gift_wisher')
	buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='gift_buyer', null=True, blank=True)
	reserver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='gift_reserver', null=True, blank=True)
	wish_list = models.ForeignKey(WishList, related_name="gift_list")
	def __unicode__(self):
		return self.title
