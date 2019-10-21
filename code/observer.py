import objectives

class Observer:
 """An observer class"""
 def __init__(self):
  """Creates the basic observer. Index will probably be made as a param at one point
  Return value:
   None"""
  self.objective_index = 0 #The current objective index

 def notify(self, action, result):
  """Notifies the objective in the list of the occurred action
  Params:
   action (int): The action that has just been performed
   result (varies): The result of the action
  Return value:
   None"""
  if objectives.objective_list[self.objective_index].notify(action, result): self.advance_own_state()

 def advance_own_state(self):
  """Advances own state
  Return value:
   None"""
  self.objective_index = objectives.objective_list[self.objective_index].finish_index

 def get_objective_description(self):
  """Returns the current objective description (goal)
  Return value:
   The current objective description"""
  return objectives.objective_list[self.objective_index].description