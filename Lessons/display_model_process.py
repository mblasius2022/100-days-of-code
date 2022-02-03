def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model: {current_design.title()}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """ Show all the models that were printed """
    print("\n\nThe following models were printed:")
    for completed_model in completed_models:
        print(f"\t- {completed_model.title()}")

