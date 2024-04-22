import os
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        result = f"Hello may name is {self.name}."
        print(result)  

    #create file that take two parameter path and filename and create file  
    def createfile(self,path,filename):
        file = path + filename
        f = open(file,"w")
        f.write("HEllo mayur file .json created")
        f.close()

    #filename=fullpathrequired
    def readfile(self,filename):
        f = open(filename,"r")
        print(f.read())
        f.close()

    #rewrite file and close it 
    #this function required fullfile path
    def rewritefile(self,filepath):
        f = open(filepath,"a")
        f.write(" Hello mayur this line append ")
        f.close()

    # "x" - Create - will create a file, returns an error if the file exist
    def createfile2(self,path,filename):
        file = path + filename
        try:
            f = open(file,"x")
        except:
            print("file already exist")
    
    def checkfileexist(self,fullfilepath):
        if os.path.exists(fullfilepath):
            print("file exist")
        else:
            print("file not exist")
    def deletefilepath(self,fullfilepath):
        if os.path.exists(fullfilepath):
            os.remove(fullfilepath)
        else:
            print("print file does not exist")

if __name__ == "__main__":
    path = "/home/mayur/Desktop/study/python_concepts/"
    filename = "demo.json"
    obj = person("mayur",26)
    
    fullfilepath = path+filename

    #print(obj.name)
    # obj.createfile(path,filename) 
       
    # obj.readfile(fullfilepath)
    # obj.rewritefile(fullfilepath)
    # obj.createfile2(path,filename) 
    # obj.checkfileexist(fullfilepath
    #obj.deletefilepath(fullfilepath)