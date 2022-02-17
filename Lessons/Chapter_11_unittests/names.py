from name_function import get_formatted_name
print("Enter 'q' to quit at any time")

while True:
    first_name = input("\nPlease enter a first name: ")
    if first_name == 'q':
        break
    last_name = input("\nPlease enter a last name: ")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first_name, last_name)
    print(f"Neatly formatted name = {formatted_name}")
