########## METHOD 1 #############
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



########## METHOD 2 #############
from itertools import product

class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings    
    def scoops(self):
        return [list(p) for p in product(self.ingredients,self.toppings)]
           

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
