# import random
# import string

# class Robot(object):
#   used_names = set()

#   def __init__(self):
#       self.reset()

#   def generate_new_random_name(self):
#     while True:
#         new_random_name = self.random_name()
#         if new_random_name not in self.used_names:
#             return new_random_name

#   def random_name(self):
#       return random.choice(string.ascii_uppercase) + \
#       random.choice(string.ascii_uppercase) + \
#       str(random.randrange(0,9)) + \
#       str(random.randrange(0,9)) + \
#       str(random.randrange(0,9))


#   def reset(self):
#       self.name = self.generate_new_random_name()
#       self.used_names.add(self.name)

  # print(random_name("lsfd1"))

import random
import string

class Robot(object):

  used_names = set()

  def __init__(self):
       self.reset()

  def generate_new_random_name(self):
      while True:
          new_random_name = self.random_name()
          if new_random_name not in self.used_names:
              return new_random_name

  def random_name(self):
      return random.choice(string.ascii_uppercase) + \
      random.choice(string.ascii_uppercase) + \
      str(random.randrange(0,9)) + \
      str(random.randrange(0,9)) + \
      str(random.randrange(0,9))

  def reset(self):
      self.name = self.generate_new_random_name()
      self.used_names.add(self.name)
      print(random_name("lsgxf"))