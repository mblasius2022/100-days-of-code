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
def make_album(title, artist, number_of_songs = None):
    album = {'title':title.title(), 'artist':artist.title(), 'number_of_songs':number_of_songs}
    return album

make_album('Sgt Pepper','beatles',10)
print()
make_album('Queen','Queen')
make_album('Thriller','Michael Jackson',15)


