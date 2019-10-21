class Objective:
 """The base objective class"""
 def __init__(self, description, finishing_conditions, finishing_index):
  """Creates a simple objective
  Params:
   description (str): The description of the objective
   finishing_conditions (dict): The conditions necessary for the objective to be counted complete
   finishing_index (int): The number of the next objective
  Return value:
   None"""
  self.description = description
  self.finishing_conditions = finishing_conditions
  self.finish_index = finishing_index

 def notify(self, action, result):
  """Tests whether a condition has been met
  Params:
   action (int): The action that has been performed
   result (varies based on objectives): The result of the said action
  Return value:
   True if the action and result match the finishing_conditions, False otherwise"""
  return action in self.finishing_conditions and result == self.finishing_conditions[action]
