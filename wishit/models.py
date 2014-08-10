from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 254)
	password = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.name

class WishList(models.Model):
	title = models.CharField(max_length = 200)
	creator = models.ForeignKey(User, related_name='wishlist_creator')
	viewers = models.ManyToManyField(User, related_name='wishlist_viewer')

class Gift(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	image = models.CharField(max_length = 200)
	wisher = models.ForeignKey(User, related_name='gift_wisher')
	buyer = models.ForeignKey(User, related_name='gift_buyer')
	reserver = models.ForeignKey(User, related_name='gift_reserver')
	wish_list = models.ForeignKey(WishList, related_name="gift_list")

	def __unicode__(self):
		return self.title
