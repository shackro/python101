# vehicles....brand model argument on vehicles .....

class vehicles:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def view(self):
        raise NotImplementedError("child class must implement")


class tayota(vehicles):
    def view(self):
        return 2.4, "million"
    #print("thank u and welcome again")

class lambongini(vehicles):
    def view(self):
        return 3.5, "million"


class ferrari(vehicles):
    def view(self):
        return 3.0, "million"

Tayota = tayota("G-5X", "Toyota")
Lambongini = lambongini("mustubi-45", "Lambongini")
ferrari = ferrari("2017-horse", "Ferrari")


print(Lambongini.brand)
print(Lambongini.model)
print(Lambongini.view())

print(Tayota.brand)
print(Tayota.model)
print(Tayota.view())

print(ferrari.brand)
print(ferrari.model)
print(ferrari.view())

