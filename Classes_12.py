# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  def self_condition(self):#method to modify condtion(variable member) value 
    self.condition = "used"
    return self.condition
  def display_car(self):
    print("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))
class ElectricCar(Car):
  def __init__(self, battery_type):
     self.battery_type = battery_type   
my_electric = ElectricCar("molten salt")
my_car = Car("DeLorean", "silver", 88)
print(my_electric.battery_type)
print(my_car.color)
print(my_car.condition)
print(my_car.mpg)