class TextInput:
    def __init__(self) :
       self.value = ""
    def  set_value(self,value):
        self.value = value

    def add(self,character):
        self.set_value(self.get_value()+character)
        
    def  get_value(self):
        return self.value
  
class NumericInput(TextInput) :
    def add(self,character):
        try:
            num  = int(character)
            self.set_value(self.get_value()+str(num))
        except:
            pass
        return self.get_value()

if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())