#name age and gender
class poeple:
    def __init__(self,name,age,gender):
        self.Name=name
        self.Age=age
        self.Gender=gender

    def display(self):
        print(self.Name,self.Age,self.Gender)

obj1=poeple("shackro arel",20,"male")
obj2=poeple("mercy mwende",19, "female")
obj3=poeple("ann kariuki",21,"female")

obj1.display()
obj2.display()
obj3.display()
