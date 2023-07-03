class fruits:
    def __init__(self, name, color, price,shape):
        self.fruitname = name
        self.fruitcolor = color
        self.fruitprice = price
        self.fruitshape = shape

    def display(self):
        print(self.fruitname, self.fruitcolor, self.fruitprice,self.fruitshape)

myobj=fruits("banana","yellow",50,"round")
myobj2=fruits("mangoes","green",100,"oval")
myobj3=fruits("apple","red",35,"round")

myobj.display()
myobj2.display()
myobj3.display()
