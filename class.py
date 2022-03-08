# all functions are called def(define) dont have to specify the object
from unicodedata import name


def sum(a,b):
    return a+b

print(sum(3,4))
# ctrl+~=terminal call and close
# ctrl+/=commentify
class Man:
    # 固定用法__init__ self
    def __init__(self):
        self.name = "Wayne"
        self.state ="Orphan"
        self.gender="veryFluid"
        self.age =21
        self.country="unknown"

    def showGender(self):
        print(self.gender)

class ManWithConstructor:
    def __init__(self, Aname, Bstatus, Cgender, Dage, Ecountry):
        self.name=Aname
        self.status=Bstatus
        self.gender=Cgender
        self.age=Dage
        self.country=Ecountry

    def showGender(self):
        print(self.gender)

    def introduceSelf(self):
        line=" ".join(["Hello my name is",self.name])
        print(line)
        print("I'm really really",self.gender,"and",self.age,sep=' ')
        line2='My name is {}, I\'m a {} person'.format(self.name,self.gender)
        print(line2)

Wayne=ManWithConstructor("Wayne","orphan","super GAY",21,"unknown")
Wayne.showGender()
Wayne.introduceSelf()

    