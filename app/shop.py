class Shop:
  def __init__(self,name,shop_id):
    self.name= name
    self.shop_id=shop_id
  
  def __str__(self):
    return ("Name: " +self.name +" Shop ID: " + str(self.shop_id))
  