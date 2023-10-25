from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
	def setUp(self):
		 objs = Menu.objects.bulk_create(
		     [
		        Menu(title="sample1", price=80, inventory=100),
		        Menu(title="samle2", price=80, inventory=100),
		     ]
		 )	

	def test_get_item(self):
		item = Menu.objects.create(title="IceCream", price=80, inventory=100)
		self.assertEqual(item.title, "IceCream")

	def  test_getall(self):
		obj_count=Menu.objects.count()
		self.assertEqual(obj_count,2)