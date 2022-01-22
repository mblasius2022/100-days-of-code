"""
Lists
"""
bicycles = ["Trek","Cannondale","Schwinn","Malvern Star","Specialized","Giant"]

print(bicycles)
print(bicycles[3])
print(bicycles[-1])

names=["mickey","minnie","goofy","Donald","Pluto","Oswald","Daisy"]
print(f"Hello {names[3].title()}")

#modify first element in names
names[0] = "Mickey Mouse"
print(names[0])

#append to names
names.append("Archie")
print(names)

#build list dynamically
motorcycles = []
motorcycles.append("Honda")
motorcycles.append("Kawasaki")
motorcycles.append("ducatti")
motorcycles.append("Suzuki")

print(motorcycles)

#insert at position 1
motorcycles.insert(0,"yamaha")
print(motorcycles)

#delete last item
del motorcycles[-1]
print(motorcycles)

#pop
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

last_motorcycle_owned = popped_motorcycle
print(f"the last bike I owned was a {last_motorcycle_owned}")

#remove by value
print(motorcycles)
motorcycles.remove("Honda")
print(motorcycles)

