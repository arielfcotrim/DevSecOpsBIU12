def get_types_list(given_list):
    """
    :param given_list
    :return: list_element_types: list of types of elements in a list
    """
    # initialize an empty list to store the types of elements in the given list
    list_element_types = []

    # iterate over the given list
    for item in given_list:
        # add the type of each element to the list
        list_element_types.append(type(item))

    return list_element_types


def print_element_types(given_list):
    """
    :return: None
    """
    given_list_msg = f"Original list: {given_list}"
    element_types_msg = f"List of element types: {get_types_list(given_list=given_list)}"

    # print the original list
    print(given_list_msg)
    # print the list of types of elements in the original list
    print(element_types_msg)


# example usage
original_list = [23, 'Python', 23.98]
print_element_types(original_list)
