class Greeter:

    def __init__(self, boss):
        self.boss = boss
        self.latest_entry = None
        self.status = False

    def enters(self, visitor):   
        self.status = True
        self.latest_entry = visitor

        return None

    def greet(self):
        if self.status == True:
            if self.latest_entry == self.boss :
                self.status = False
                return "Hello, %s" %self.latest_entry
            else:
                self.status = False
                return "Welcome, %s" %self.latest_entry
        else:
            return None
    
if __name__ == "__main__":
    g = Greeter('Chuck')
    g.enters('John')
    print(g.greet())