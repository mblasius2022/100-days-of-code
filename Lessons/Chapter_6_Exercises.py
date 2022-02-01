"""
Chapter 6 - Dictionaries

#6.1
person_0 = {'first_name':'John', 'last_name':'Doe', 'age':'53', 'city':'Perth'}
print(person_0)
print(person_0['first_name'])

#6.2
favourite_numbers = {'bob':'37','beetlejuice':'13', 'rosie':'18', 'stanley':'42', 'goofy':'42'}
print(f"Bob's favourite number is {favourite_numbers['bob']}")

#6.3
programming_terms = {
    'integer':'a whole number',
    'float':'a decimal number',
    'variable':'used to store a value',
    'dictionary':'a collection of key value pairs',
    'list':'a collection of itmes in a particular order'
    }
print(f"Integer:\n\t{programming_terms['integer']}")
print(f"Float:\n\t{programming_terms['float']}")
print(f"Variable:\n\t{programming_terms['variable']}")
print(f"Dictionary:\n\t{programming_terms['dictionary']}")
print(f"List:\n\t{programming_terms['list']}")


#6.4
programming_terms = {
    'integer':'a whole number',
    'float':'a decimal number',
    'variable':'used to store a value',
    'dictionary':'a collection of key value pairs',
    'list':'a collection of itmes in a particular order'
    }

for k,v in programming_terms.items():
    print(f"\n{k.title()}:\t{v}")

programming_terms['comments'] = 'Comments are code lines that will not be executed'
programming_terms['tuple'] = 'A tuple is an ordered, and unchangeable, collection'
programming_terms['elif'] = 'elif is the same as "else if" in other programming languages'

for k,v in programming_terms.items():
    print(f"\n{k.title()}:\n\t{v}")


#6.5 Rivers
rivers = {
    'nile':'egypt',
    'ganges':'india',
    'murray':'australia',
    'colorado':'usa',
    'amazon':'brazil'
}
for k,v in rivers.items():
    print(f"The {k.title()} runs through {v.title()}")

for key in rivers.keys():
    print(f"\n{key.title()}")

for value in rivers.values():
    if value.lower() == 'usa':
        print(f"\n{value.upper()}")
    else:
        print(f"\n{value.title()}")


#6.6 Polling
favourite_languages = {
    'stanley':'python',
    'symone':'HTML and CSS',
    'anna':'C#',
    'mario':'javascript'
}

names_for_survey = ['bob','stanley', 'john', 'oswald', 'goofy', 'alma']

for name in names_for_survey:
    if name not in favourite_languages.keys():
        print(f"Please take our poll {name.title()}")
    else:
        print(f"Thank you for taking our poll {name.title()}" )


#6.7
person_0 = {'first_name':'Mickey', 'last_name':'Mouse', 'age':'94', 'city':'Orlando'}
person_1 = {'first_name':'Minnie', 'last_name':'Mouse', 'age':'94', 'city':'Orlando'}
person_2 = {'first_name':'Goofy', 'last_name':'', 'age':'90', 'city':'Orlando'}
people = [person_0, person_1, person_2]
for person in people:
    print(person)
"""

"""
#6.8 pets
pet_0 = {'name':'pluto','type':'dog','owner':'Mickey Mouse'}
pet_1 = {'name':'muttle','type':'dog','owner':'Dick Dastardly'}
pet_2 = {'name':'scooby doo','type':'dog','owner':'Shaggy'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(pet)
"""

"""
#6.9
favourite_places = {'mickey':['Orlando','Los Angeles','Paris'], 'minnie':['Orlando','Anaheim','HongKong'],'goofy':['Tokyo','Hong Kong','Paris']}
for name, places in favourite_places.items():
    print(f"{name.title()}'s favourite places are:")
    for place in places:
        print(f"\t{place}")
"""

#6.1 Cities
cities= {
    'mumbai':{
        'state':'Maharashtra',
        'area':'603 sqKM',
        'population':'12,478,447',
        'country':'india'
        },
    'tokyo':{
        'state':'Kanto',
        'area':'2194 sqKM',
        'population':'14,043,239',
        'country':'japan'
        },
    }

for city, statistics in cities.items():
    print(f"\n{city.title()}:")
    print(f"\tState: {statistics['state'].title()}")
    print(f"\tArea: {statistics['area']}")
    print(f"\tPopulation: {statistics['population']}")
    print(f"\tCountry: {statistics['country'].title()}")




