# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)
hippo = Animal("Gury", 6)
slot = Animal("Gin", 9)
ocelot = Animal("Tonic", 11)
print(hippo.health, slot.health, ocelot.health)
hippo.description()

class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print(product + " added.")
    else:
      print(product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print(product + " removed.")
    else:
      print(product + " is not in the cart.")
my_cart = ShoppingCart('pijama')
my_cart.add_item('Ericson', 12)

print("end")

class Person:
  def __init__(self, name):
    self.name = name
  def calculate_wage(self, hours):
      self.hours = hours
      return hours * 8 
  def hours_week(self, week):
      self.week = week
      return week * 5
     
class Student(Person):

    def calculate_wage(self,hours):
        self.hours = hours 
        return hours * 6 
    def hours_week(self, week):
        self.week = week 
        return week * 4
    def parent_back(self, hours):
        return super(Student, self).calculate_wage(hours)
    
stud = Student("John")  
print("My name is " + stud.name)
print(stud.parent_back(10))


