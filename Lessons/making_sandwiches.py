def make_sandwich(*ingredients):
    """ Simulates making a sandwich """
    print("\nMaking a sandwich with:")
    for ingredient in ingredients:
        print(f"\t- {ingredient.title()}")
