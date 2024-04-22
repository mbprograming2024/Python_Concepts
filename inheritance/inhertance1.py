class parent:
    def __init__(self,fname,lname):
        self.firstname= fname
        self.lastname = lname
        print(self.firstname,self.lastname)
    def details1(self):
        print(self.firstname,self.lastname)

class Son(parent):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year=year
        print(fname,lname,year)
    def details(self):
        super().details()
        print(self.firstname,self.lastname,self.year)
class Grenddoughter(Son):
    year = 2021
    def __init__(self,fname,lname,city):
        super().__init__(fname,lname,self.year)
        print(city)



if __name__ == "__main__":
    # obj = parent("Mayur","Baviskar")
    # obj.detials()    
    
    # obj2 = Son("Mayur","Baviskar",1995)
    # obj2.details1()

    obj3 = Grenddoughter("Mayur","Baviskar","Nasik")