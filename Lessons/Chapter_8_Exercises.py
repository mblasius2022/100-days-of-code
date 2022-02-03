"""
Chapter 8 - Functions
"""
#8.1
# def display_message():
#     x = 1
#     while x < 5:
#         print("Chapter 8 - Functions")
#         x += 1

# display_message()

#8.2 - Favourite Book
# def favourite_book(title):
#     print(f"\tyour favourite book is {title.title()}\n")

# x = 1
# while x < 5:
#     book = input("What is your favourite book?: ")
#     favourite_book(book)
#     x += 1

#8.3 T shirts
# def order_shirts(size, message):
#     print(f"\nYou have ordered the following T shirt\n\tSize: {size.upper()}\n\tLogo: {message.title()}")

# x = 1
# while x <= 3:
#     tshirt_size = input("Choose Size eg XXL: ")
#     message = input("Enter Message or Logo for T-Shirt: ")
#     order_shirts(tshirt_size, message)
#     x += 1

# order_shirts(message = "Wasn't Me", size = 'XXL')

#8.4
# def order_shirts(size = 'Large', message = 'I love Python'):
#     print(f"\nYou have ordered the following T shirt\n\tSize: {size.upper()}\n\tLogo: {message.title()}")

# order_shirts()
# order_shirts(size ='Medium')
# order_shirts(size ='Small', message = 'Hello World')
# order_shirts('xxl', 'Chill Out Dude')


#8.5
# def city_information(city, country = 'India'):
#     print(f"{city.title()} is in {country.title()}")

# city_information('Sydney','Australia')
# city_information('Mumbai')
# city_information('tokyo','Japan')
# city_information('paris','france')

#8.6
# def city_information(city, country):
#     formatted_city = city.title() + ',' + country.title()
#     return formatted_city


# cities  = {'mumbai':'india', 'tokyo':'japan', 'paris':'france','Sydney':'Australia'}
# for city, country in cities.items():
#     returned_city = city_information(city, country)
#     print(f"\n{returned_city}")

#8.7
# def make_album(title, artist, number_of_songs = None):
#     albums = {'title':title.title(), 'artist':artist.title(), 'number_of_songs':number_of_songs}
#     return albums

# album = make_album('Sgt Pepper','beatles',10)
# print(album)
# album = make_album('Queen','Queen')
# print(album)
# album = make_album('Thriller','Michael Jackson',15)
# print(album)


#8.8
# albums= {}
# def make_album(name,title, artist):
#     album = {'title':title.title(), 'artist':artist.title()}
#     albums[name] = album
#     return album

# while True:
#     your_name = input("Enter your name\n(enter q to quit): ")
#     if your_name.lower() == 'q':
#         break
#     else:
#         album_title = input("Enter Name of Album: ")
#         album_artist = input("Enter Name of Artist: ")
#         album = make_album(your_name, album_title,album_artist)
#         print(album)

# for owner, album in albums.items():
#     print(f"\nAlbum owned by {owner}")
#     print(f"\t{album['title']} by {album['artist']}")

#8.9
# def show_messages(messages):
#     for message in messages:
#         print(message)

# message_list = ['Hello World', 'Good Evening', 'Salute', "G'day"]
# show_messages(message_list)

#8.10


# def send_messages(unsent_messages,sent_messages):
#     while unsent_messages:
#         current_message = unsent_messages.pop()
#         print(f"Sending Message: {current_message}")
#         sent_messages.append(current_message)

# unsent_messages = ['Hello World', 'Good Evening', 'Salute', "G'day"]
# sent_messages = []

# print(f"Original Unsent Messages: {unsent_messages}")
# print(f"Original Sent Messages: {sent_messages}\n\n")
# send_messages(unsent_messages,sent_messages)
# print(unsent_messages)
# print(sent_messages)


#8.11
# def send_messages(unsent_messages, sent_messages):
#     while unsent_messages:
#         current_message = unsent_messages.pop()
#         print(f"Sending Message: {current_message}")
#         sent_messages.append(current_message)

# unsent_messages = ['Hello World', 'Good Evening', 'Salute', "G'day"]
# sent_messages = []

# print(f"Original Unsent Messages: {unsent_messages}")
# print(f"Original Sent Messages: {sent_messages}\n\n")
# send_messages(unsent_messages[:],sent_messages)
# print(unsent_messages)
# print(sent_messages)

#8.12
# def make_sandwich(*ingredients):
#     print("\nMaking a sandwich with:")
#     for ingredient in ingredients:
#         print(f"\t- {ingredient.title()}")

# make_sandwich('ham')
# make_sandwich('bacon', 'lettuce', 'tomato')
# make_sandwich('cheese', 'salad')


#8.13
# user_info = {}
# def build_profile(first_name, last_name, **user_info):
#     user_info['first_name'] = first_name.title()
#     user_info['last_name'] = last_name.upper()
#     return user_info

# user_profile = build_profile('John','Doe', city = 'Perth', phone = '0400000000', age = 99, occupation = 'Liquor Baron')
# print(user_profile)
# for k,v in user_profile.items():
#     print(f"{k} : {v}")

#8.14
# car_info = {}
# def make_car(brand,**car_info):
#     car_info['brand'] =  brand
#     return car_info

# car = make_car('Volkswagen',model = 'Beetle',color = 'yellow', year = 1974, tow_package = False, sat_nav = False, roof_racks = True)
# for k, v in car.items():
#     print(f"{k} = {v}")

#8.15
# from display_model_process import *
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron', 'godzilla']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

#8.16
from making_sandwiches import make_sandwich
make_sandwich('bacon', 'lettuce', 'tomato', 'cheese', 'jalapeno')

from making_sandwiches import make_sandwich as ms
make_sandwich('pastrami', 'pickle')

import making_sandwiches as mn
mn.make_sandwich('2 all beef patties', 'lettuce', 'pickles', 'onion', 'special sauce')

from making_sandwiches import *
make_sandwich('toasted', 'cheese', 'ham', 'tomato')
