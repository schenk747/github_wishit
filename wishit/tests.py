import datetime
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase

from wishit.models import Gift, User, WishList

def create_user():
	return User.objects.create(name='Nissefar', email='nisse@far.com', password='nisseword')


def create_wishlist():
	return WishList.objects.create(title='list_of_wishes', creator=User.objects.get(id=1))

def create_gift(text):
	create_user()
	create_wishlist()
	#user = User.objects.get(name='Nissefar')
	#User.objects.create(name='Nissefar', email='nisse@far.com', password='nisseword')
	user = User.objects.get(name='Nissefar')
	#WishList.objects.create(title='list_of_wishes', creator=user)
	wl = WishList.objects.get(title='list_of_wishes')
	wl.viewers.add(user)
	return Gift.objects.create(title='Baad', text=text, image='billede.jpg', wisher=user, buyer=user, reserver=user, wish_list=WishList.objects.get(id=1))

class WishItTests(TestCase):
	def test_index_view_with_no_gifts(self):
		"""If no gifts exist, an appropriate message should be displayed"""
		gift = create_gift('nisse')
		us = User.objects.get(id=1)
		g = Gift.objects.get(title='Baad')
		response = self.client.get(reverse('wishit:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No gifts available.")
		self.assertQuerysetEqual(response.context['gift_list'], [])
		print gift_list

class GiftMethodTests(TestCase):
	def test_title_is_not_empty(self):
		"""
		Test that title is not empty
		p"""
		gift_test = Gift(title = 'Speedbaad')
		self.assertTrue(gift_test.title)


