class animal:
    def __init__(self, name,color):
        self.name = name
        self.color=color

    def speak(self):
        raise NotImplementedError("chald classes must implement")


class dog(animal):
    def speak(self):
        return "woof!"


class cat(animal):
    def speak(self):
        return "meow!"

class cow(animal):
    def speak(self):
        return "moooo!"



# create an onject
Dog = dog("shalook","BROWN")
CAT=cat("shilaa","WHITE")
Cow=cow("honabell","Greywhite")


print(Dog.name)
print(Dog.speak())
print(CAT.name)
print(CAT.speak())
print(Cow.name)
print(Cow.color)
print(Cow.speak())