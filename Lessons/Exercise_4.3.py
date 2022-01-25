"""
Numerical lists


#count to 20
for number in range (1,21):
    print(number)
    
#one million
for number in range(1,1000001):
    print(number)
 
#summing a million
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))


# odd numbers between 1 and 20
for number in range(1,21,2):
    print(number)
"""

#multiples of threes
threes = [value * 3 for value in range (1,31)]
print(threes)
for three in threes:
    print(three)
 
print("\nprinting multiples of 3 for numbers between 1 and 30 inclusive:")   
for three in range(1,31):
    print (three*3)
    

"""
#cubes
cubes = [value **3 for value in range(1,11)]
print(f"the min of cubes = {min(cubes)} and the max = {max(cubes)}")
max(cubes)
print(cubes)
for cube in cubes:
    print(cube)

"""

#Cube Comprehension
cubes = [value **3 for value in range(1,11)]
print(cubes)