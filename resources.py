# Initialize resources with a default value
resources = {
    'resources': 1
}


def display_resources():
    """
    Display the current amount of resources.
    """
    print("\nCurrent Resources Status:")
    for resource, amount in resources.items():
        print(f"{resource.capitalize()}: {amount}")
    print()


def update_resource(amount):
    """
    Update resources by adding or subtracting an amount.
    """
    resources['resources'] += amount
    # Ensure resources do not drop below zero
    if resources['resources'] < 0:
        resources['resources'] = 0
    print(f"\nUpdated resources by {amount}.")


def get_resource_amount():
    """
    Get the current amount of resources.
    """
    return resources['resources']


def use_resource():
    """
    Use a resource, typically for a specific action.
    """
    if resources['resources'] > 0:
        resources['resources'] -= 1
        print("\nUsed one resource.")
    else:
        print("\nNo resources available to use.")
