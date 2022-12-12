
###################################################################################################

# students = [("Allen Anderson", "Computer Science"),
#             ("Edgar Einstein", "Engineering"),
#             ("Farrah Finn", "Fine Arts")]


# # print(students[0][0])

# a = ("Allen Anderson", "Computer Science")
# a[0] = "Ad"

###################################################################################################

# class IceCreamMachine:
    
#     def __init__(self, ingredients, toppings):
#         self.ingredients = ingredients
#         self.toppings = toppings
        
#     def scoops(self):
#         if len(self.ingredients)==0 or len(self.toppings)==0 :
#             return []
#         else:
#             final_list = []
#             for ing in self.ingredients :
#                 for tp in self.toppings:
#                     sample = []
#                     sample.append(ing)
#                     sample.append(tp)
#                     final_list.append(sample)
#             return final_list

# if __name__ == "__main__":
#     machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
#     print(machine.scoops()) #should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]


###################################################################################################

# class IceCreamMachine:
    
#     def __init__(self, ingredients, toppings):
#         self.ingredients = ingredients
#         self.toppings = toppings
        
#     def scoops(self):
#         if len(self.ingredients)==0 or len(self.toppings)==0 :
#             return []
#         else:
#             final_list = []
#             for ing in self.ingredients :
#                 for tp in self.toppings:
#                     sample = []
#                     sample.append(ing)
#                     sample.append(tp)
#                     final_list.append(sample)
#             return final_list

# if __name__ == "__main__":
#     machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
#     print(machine.scoops()) #should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]


###################################################################################################

# def pipeline(*funcs):
#     def helper(arg):
#         x = arg
#         for f in funcs:
#             x = f(x)
#         return x
#     return helper
            
# fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)

# print(fun(3))
# #print(fun(3)) #should print 5.0

###################################################################################################

# import math

# def find_roots(a, b, c):
#     x1 =  ((math.sqrt(b*b-4*a*c)) - b)/(2*a)
#     x2 =   (- (math.sqrt(b*b-4*a*c)) - b)/(2*a)
#     return (x1,x2)
# print(find_roots(2, 10, 8))


###################################################################################################

# from itertools import chain

# def unique_names(names1, names2):
#     print(chain(names1,names2))
#     return list(set(chain(names1, names2)))

# if __name__ == "__main__":
#     names1 = ["Ava", "Ava", "Olivia"]
#     names2 = ["Olivia", "Ava", "Emma"]
#     print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia


###################################################################################################

# def group_by_owners(files):
#     final_dict = {}
#     for key,value in files.items():
#         if value not in list(final_dict.keys()):
#             final_dict[value] = []
#             final_dict[value].append(key)
#         else:
#             final_dict[value].append(key)
#     return final_dict
        
# if __name__ == "__main__":    
#     files = {
#         'Input.txt': 'Randy',
#         'Code.py': 'Stan',
#         'Output.txt': 'Randy'
#     }   
#     print(group_by_owners(files))


###################################################################################################

# import math

# def add_patch():
#     # Write the code that goes here
#     def log100(x):
#         return math.log(x,100)
#     math.log100 = log100
        
# # Example case.
# add_patch()      
# print(math.log100(10))

###################################################################################################

# def match_key_combo(sequence):
#     q_count = 0
#     z_count = 0
#     sequence_upper = sequence.upper()

#     for i in range(0,len(sequence_upper)-2):
#             if(sequence_upper[i]+sequence_upper[i+1]+sequence_upper[i+2]=="QEE"):
#                 q_count+=1
#             if(sequence_upper[i]+sequence_upper[i+1]+sequence_upper[i+2]=="ZCC"):
#                 z_count+=1
#     print(q_count)
#     print(z_count)
    
#     if(q_count == z_count):
#         return True
#     elif (q_count==0 and z_count==0):
#         return True
#     elif(q_count != z_count):
#         return False

# print(match_key_combo('QEEAZCC'))

###################################################################################################

# def tuple_slice(startIndex, endIndex, tup):
#     sl = ""
#     for i in range(startIndex,endIndex):
#         if i != endIndex-1:
#             sl+=str(tup[i])+","
#         else:
#             sl+=str(tup[i])

#     return sl

# if __name__ == "__main__":
#     print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))

###################################################################################################

# from abc import ABC, abstractmethod

# class DriverExam:
#     @staticmethod
#     def execute_exercise(exercise):
#         """
#         :param exercise: (object) The object of a class
#             implementing ExerciseInterface
#         """
#         try:
#             exercise.start()
#             exercise.execute()
#         except:
#             exercise.mark_negative_points()
#         finally:
#             exercise.end()

# class ExerciseInterface(ABC): 
#     @abstractmethod
#     def start(self):
#         pass
    
#     @abstractmethod
#     def execute(self):
#         pass
      
#     @abstractmethod
#     def mark_negative_points(self):
#         pass
      
#     @abstractmethod
#     def end(self):
#         pass
    
# class Exercise(ExerciseInterface):
#     def start(self):
#         print("start")
#     def execute(self):
#         print("execute")
#     def mark_negative_points(self):
#         print("mark_negative_points")
#     def end(self):
#         print("end")
    
# print(DriverExam().execute_exercise(Exercise()))

###################################################################################################

# class ChineseBox:
#     count = 0
#     def __init__(self, contained_box = None):
#         self.contained_box = contained_box
#         if (self.contained_box != None):
#             ChineseBox.count +=1
#             self.number_of_smaller_boxes()
        
#     def number_of_smaller_boxes(self):
#         return ChineseBox.count


# if __name__ == "__main__":
#     box = ChineseBox(ChineseBox())
#     print(box.number_of_smaller_boxes())

###################################################################################################

# from collections import defaultdict

# class RewardPoints:
#     def __init__(self):
#         self.customers = defaultdict(int)
        
#     def earn_points(self, customer_name, points):
#         if(self.customers[customer_name]==0 and points>0):
#             self.customers[customer_name]=500
        
#         if(points<=0):
#             pass

#         self.customers[customer_name] += points
    
#     def spend_points(self, customer_name, points):
#         if customer_name not in self.customers:
#             self.customers[customer_name] = 0
#         else:
#             if(points<=0):
#                 pass
#             elif(points>self.customers[customer_name]):
#                 pass
#             else:
#                 self.customers[customer_name] -= points
#         return self.customers[customer_name]
        
# if __name__ == "__main__":
#     rewardPoints = RewardPoints()
#     rewardPoints.earn_points('John', 520)
#     print(rewardPoints.spend_points('John', 200))

###################################################################################################

# import math
# def areas(r, a):
#     """
#     :param r: (float) The radius of the circle.
#     :param a: (float) The angle of the segment.
#     :returns: (list) (A list of two elements containing the area inside, and area outside the circle, in that order.)
#     """
#     area_of_circle = math.pi * r * r
#     area_of_segment = (r**2/2)* ((a*math.pi/180)-math.sin(a*math.pi/180)) 

#     return (area_of_segment,area_of_circle-area_of_segment)

# print(areas(10, 90))

###################################################################################################

# from collections import deque

# class Veterinarian:
#     def __init__(self):
#         self.stack = deque()
#     def accept(self, petName):
#         self.stack.append(petName)

#     def heal(self):
#         return self.stack.popleft()

# if __name__ == "__main__":
#     veterinarian = Veterinarian()
#     veterinarian.accept("Barkley")
#     veterinarian.accept("Mittens")
#     print(veterinarian.heal()) # Should print: Barley
#     print(veterinarian.heal()) # Should print: Mittens

###################################################################################################

# def find_max_sum(numbers):
#     m1 = max(numbers)
#     numbers.remove(m1)
#     m2 = max(numbers)
#     return m1+ m2

# if __name__ == "__main__":
#     print(find_max_sum([5, 9, 7, 11]))

# def find_max_sum(numbers):
#     return sum(sorted(numbers)[-2:])

# if __name__ == "__main__":
#     print(find_max_sum([5, 9, 7, 11]))

###################################################################################################

# import io

# def get_occurrence_count(to_search, stream):
#     """
#     :param to_search: (String) The text to search for
#     :param stream: (StringIO) An in-memory stream for text I/O
#     :returns: (int) The number of lines that contain to_search
#     """
#     a = stream.getvalue()
#     return a.count(to_search)

# if __name__ == "__main__":
#     stream = io.StringIO("Hey! How are you?\nI am good, how about you?\nI am good too.")
#     print(get_occurrence_count('good', stream))
#     stream.close()

###################################################################################################

# class CropRatio:

#     def __init__(self):
#         self._crops = {}
#         self._total_weight = 0

#     def add(self, name, crop_weight):
#         curr_crop_weight = 0
#         if name not in self._crops:
#             self._crops[name] = curr_crop_weight
#         curr_crop_weight = self._crops[name] + crop_weight
#         self._crops[name] = curr_crop_weight
#         self._total_weight += crop_weight

#     def proportion(self, name):
#         if name not in self._crops:
#             return 0
#         else:
#             return self._crops[name]/self._total_weight

# if __name__ == "__main__":
#     crop_ratio = CropRatio()
#     crop_ratio.add('Wheat', 5)
#     crop_ratio.add('Wheat', 4)
#     crop_ratio.add('Rice', 1)
#     print(crop_ratio.proportion('Wheat'))

###################################################################################################

# import collections

# Node = collections.namedtuple('Node', ['left', 'right', 'value'])


# def contains(root, value):
#     if root is None:
#         return False
#     elif root.value == value:
#         return True
#     elif root.value >= value:
#         return contains(root.left, value)
#     else:
#         return contains(root.right, value)


# n1 = Node(value=1, left=None, right=None)
# n3 = Node(value=3, left=None, right=None)
# n2 = Node(value=2, left=n1, right=n3)

# print(contains(n2, 3))

#######################################################################################

# class TextInput:
#     def __init__(self) :
#        self.value = ""
#     def  set_value(self,value):
#         self.value = value

#     def add(self,character):
#         self.set_value(self.get_value()+character)
        
#     def  get_value(self):
#         return self.value
  
# class NumericInput(TextInput) :
#     def add(self,character):
#         try:
#             num  = int(character)
#             self.set_value(self.get_value()+str(num))
#         except:
#             pass
#         return self.get_value()

# if __name__ == '__main__':
#     input = NumericInput()
#     input.add("1")
#     input.add("a")
#     input.add("0")
#     print(input.get_value())

#######################################################################################

# class Song:
#     def __init__(self, name):
#         self.name = name
#         self.next = None

#     def next_song(self, song):
#         self.next = song 
    
#     def is_in_repeating_playlist(self):
#         """
#         :returns: (bool) True if the playlist is repeating, False if not.
#         """
#         if self.next is None:
#             return False
#         song_list = set()
#         current = self
        
#         while True:
#             if current.next is None:
#                 return False
#             elif current.next.name not in song_list:
#                 song_list.add(current.name)
#                 current = current.next
#             else:
#                 return True    

# first = Song("Hello")
# second = Song("Eye of the tiger")
    
# first.next_song(second)
# second.next_song(first)
    
# print(first.is_in_repeating_playlist())

#######################################################################################

# class DocumentStore(object):

#     def __init__(self, capacity):
#         self._capacity = capacity
#         self._documents = []

#     @property
#     def capacity(self):
#         return self._capacity

#     @property
#     def documents(self):
#         return self._documents

#     def add_document(self, document):
#         if len(self._documents) >= self._capacity:
#             raise Exception('Document store is full')
#         self._documents.append(document)

#     def __repr__(self):
#         return "Document store: " + str(len(self._documents)) + "/" + str(self._capacity)


# # To see the output, uncomment the lines belows:
# document_store = DocumentStore(2)
# document_store.add_document("document")
# print(document_store)

########################################################################################

# def minimal_number_of_packages(items, available_large_packages, available_small_packages):
#     if(items>available_large_packages*5+available_small_packages):
#         return -1
#     possible_large = (int(items/5))
#     if(available_large_packages>=possible_large):
#         count = possible_large
#         possible_small = items - 5*count 
#         count += possible_small
#     else:
#         count = available_large_packages
#         possible_small = items - 5*count
#         count+=possible_small

#     return count
    
# print(minimal_number_of_packages(16, 2, 10))

########################################################################################

# class Greeter:

#     def __init__(self, boss):
#         self.boss = boss
#         self.latest_entry = None
#         self.status = False

#     def enters(self, visitor):   
#         self.status = True
#         self.latest_entry = visitor

#         return None

#     def greet(self):
#         if self.status == True:
#             if self.latest_entry == self.boss :
#                 self.status = False
#                 return "Hello, %s" %self.latest_entry
#             else:
#                 self.status = False
#                 return "Welcome, %s" %self.latest_entry
#         else:
#             return None
    
# if __name__ == "__main__":
#     g = Greeter('Chuck')
#     g.enters('John')
#     print(g.greet())

########################################################################################

# from collections import namedtuple
# from functools import reduce
# from itertools import chain
# from operator import add

# def merge(*records):
#     """
#     :param records: (varargs list of namedtuple) The patient details.
#     :returns: (namedtuple) named Patient, containing details from all records, in entry order.
#     """ 
#     cls = namedtuple("Patient", reduce(add, (arg._fields for arg in records)))
#     #cls = namedtuple("_".join(arg.__class__.__name__ for arg in records), reduce(add, (arg._fields for arg in records)))

#     return cls(*chain(*records))
#     # return None
    
# PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
# personal_details = PersonalDetails(date_of_birth = '06-04-1972')
                                   
# Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
# complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')
  
# print(merge(personal_details, complexion))

########################################################################################

# def find_all_hobbyists(hobby, hobbies):
#     final_list = []
#     for person in hobbies:
#         if hobby in hobbies[person]:
#             final_list.append(person)
#     return final_list 

# if __name__ == "__main__":
#     hobbies = { 
#         "Steve": ['Fashion', 'Piano', 'Reading'],
#         "Patty": ['Drama', 'Magic', 'Pets'],
#         "Chad": ['Puzzles', 'Pets', 'Yoga']
#     }
    
#     print(find_all_hobbyists('Yoga', hobbies))

########################################################################################


import random

def init(n):
    yield random.seed(n)
    # randomlist = []
    # for i in range(0,n):
    #     a = random.randint(1,30)
    #     randomlist.append(n)
    # print(randomlist)

if __name__ == "__main__":
    generators = init(5)
    if generators is not None:
        for rnd in generators:
            print(rnd.randint(0, 1000))
