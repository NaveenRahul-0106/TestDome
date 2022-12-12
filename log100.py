import math

def add_patch():
    # Write the code that goes here
    def log100(x):
        return math.log(x,100)
    math.log100 = log100
        
# Example case.
add_patch()      
print(math.log100(10))