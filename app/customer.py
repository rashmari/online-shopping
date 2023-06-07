class Customer:
  def __init__(self,fname,lname,cutomer_id,email):
    self.fname=fname
    self.lname=lname
    self.cutomer_id=cutomer_id
    self.email=email

  def __str__(self):
    return ("FirstName: " + self.fname + "LastName: " + self.lname + "CustomerID: " + str(self.cutomer_id) + "Email: " + self.email)
  