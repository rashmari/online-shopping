import unittest
from shop import Shop
from customer import Customer

class ShopTest(unittest.TestCase):
  def test_shop_created_correctly(self):
    shop_name = "Test Shop"
    shop_id = 1
    shop = Shop(shop_name, shop_id)

    self.assertEqual(shop_name, shop.name)
    self.assertEqual(shop_id, shop.shop_id)

  def test_shop_has_correct_str(self):
    shop_name = "Test Shop"
    shop_id = 1
    shop = Shop(shop_name, shop_id)

    self.assertEqual("Name: Test Shop Shop ID: 1", str(shop))

class CustomerTest(unittest.TestCase):

  def test_customer_created(self):
    fname="Rashmi"
    lname="Kumari"
    customerid='1'
    email="rashmi25346@gmail.com"
    customer= Customer(fname,lname,customerid,email)

    self.assertEqual(fname, customer.fname)




if __name__ == '__main__':
  unittest.main()