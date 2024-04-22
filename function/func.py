
class func:
    def add(self,a,b):
        c = a + b
        print(c)
        
    def add(self,a,b=3):
        c = a + b
        print(c)
    def add(self,a=5,b=3):
        c = a + b
        print(c)
    def add(self,*a):
        d=0
        for i in a:
            d = d+i 
        print(d) 
    #     Keyword Arguments
    # You can also send arguments with the key = value syntax.
          
if __name__ == "__main__":
    obj = func()
    # obj.add(2,3)
    # obj.add()
    # obj.add(9)
    # obj.add(1,2,3,4,5,6,7,8,9)
    obj.add(6,9)