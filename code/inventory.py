class Inventory:
 """The inventory class"""
 def __init__(self):
  """Creates an inventory"""
  self._items = {} #Items in the inventory, _items because of the property below
  self.index = 0 #inventory position

 @property
 def items(self):
  """Returns the items and their values
  Return value:
   a dict with the item names being the key, and item values being the value of the said key"""
  return self._items

 @items.setter
 def items(self, inv):
  """A quick overwrite method for the inventory, handy for loading a game
  Return Value:
   None"""
  self._items = inv

 def cycle(self, direction):
  """Cycles the inventory, used for when the player wants to look through their items
  Params:
   direction (int, 1:-1): The direction the inventory must be cycled to
  Return value:
   The new item name and the current quantity of the said item in the inventory"""
  if len(self._items) == 0: return "Nothing"
  self.index += direction
  #Prevent out of bound index
  if self.index == len(self._items): self.index = 0
  elif self.index == -1: self.index = len(self._items) - 1
  return self.get_item()

 def get_item(self):
  """Retrieves the current item in the inventory and returns it's name and value
  Return value:
   Item name and it's value"""
  return list(self._items.keys())[self.index] + ": " + str(self._items[list(self._items.keys())[self.index]])

 def add_item(self, name, value):
  """Adds an item to the inventory. Can also be used to increase the number of the said item if the name is found to be present in the inventory
  Params:
   Name (str): The name of the item
   value (int): The amount of the ite, the inventory will contain
   Return value:
   None"""
  if name not in self._items: self._items[name] = value
  else: self._items[name] += value

 def use_item(self):
  """Uses an item in the inventory. Yet to be implemented
  Return value:
   None"""
  pass
