class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")
 

loc = Location("Artem", "Valencia")

print(loc.name)
print(loc.country)
print(type(loc))

##
loc1 = Location("Tomas", "Portugal")
loc1.myLocation()
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
your_loc = Location("Artem", "Valencia")

loc2.myLocation()
loc3.myLocation()
your_loc.myLocation()
