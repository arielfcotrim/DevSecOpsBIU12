# this python script does manipulations to a list of numbers

def get_sum(numbers):
    """
    :param numbers: A list of numbers.
    :return: total: The sum of the numbers in the list.
    """

    # The sum function is called on the list of numbers, which returns the sum of all the elements in the list
    total = sum(numbers)

    return total


def get_highest_num(numbers):
    """
    :param numbers: A list of numbers.
    :return: highest_num: The highest number in the list.
    """

    # Use the max() function to get the highest number in the list
    highest_num = max(numbers)

    return highest_num


def get_lowest_num(numbers):
    """
    :param numbers: A list of numbers.
    :return: lowest_num: The lowest number in the list.
    """

    # Use the min() function to get the lowest number in the list
    lowest_num = min(numbers)

    return lowest_num


def get_average(numbers):
    """
    :param numbers: A list of numbers.
    :return: average: The average of the numbers in the list.
    """

    # The get_sum function is called on the list of numbers, which returns the sum of all the elements in the list
    total = get_sum(numbers)

    # The average is calculated by dividing the sum of the numbers by the number of numbers in the list
    average = total / len(numbers)

    return average


def get_numbers_mid_removed(numbers):
    """
    :param: numbers: A list of numbers.
    :return: numbers_mid_removed: A list of numbers with the middle number/s of the original list removed.
    """

    # The size of the list is calculated by getting the length of the list
    size = len(numbers)

    # The middle number/s of the list is removed by slicing the list
    # If the size of the list is even, the two middle numbers are removed
    if size % 2 == 0:
        # subtract 1 from the middle index to jump over to the left to remove the middle number on the left
        left_side = numbers[:size // 2 - 1]
        # add 1 to the middle index to jump over to the right to remove the middle number on the right
        right_side = numbers[(size // 2) + 1:]

    # If the size of the list is odd, the middle number is removed
    else:
        # slice the list from the beginning to the middle index (exclusive)
        left_side = numbers[:(size // 2)]
        # add 1 to the middle index to jump over the middle index number
        right_side = numbers[(size // 2) + 1:]

    # The left and right sides of the list are concatenated to form a new list with the middle number/s removed
    numbers_mid_removed = left_side + right_side

    return numbers_mid_removed


def sort_numbers(numbers):
    """
    :param numbers: A list of numbers.
    :return: numbers_sorted: A list of numbers sorted in ascending order
    """

    # The sorted() function is called on the list of numbers
    numbers_sorted = sorted(numbers)

    return numbers_sorted


def print_numbers_x_times(numbers, loops):
    """
    :param numbers: A list of numbers.
    :param loops: An integer representing the number of times to print the list
    :return: None.
    """

    # The list of numbers is printed x number of times, depending on the value of 'loops'
    for i in range(loops):
        print(numbers)


def get_numbers_from_x_index(numbers, index):
    """
    :param numbers: A list of numbers.
    :param index: An integer representing the index position to start from.
    :return: numbers_after_x_index: A list of numbers after the given index position.
    """

    # The list of numbers is sliced from the given index position to the end of the list
    numbers_after_x_index = numbers[index:]

    return numbers_after_x_index


def print_numbers_smaller_than_avg(numbers):
    """
    :param numbers: A list of numbers.
    :return: numbers_smaller_than_avg: A list of numbers smaller than the average of the sum of the original list
    """

    # The average of the sum of the numbers in the list is calculated by calling the get_average function
    average = get_average(numbers)

    # A new list is created to store the numbers smaller than the average
    numbers_smaller_than_avg = []
    # Each number in the list is checked to see if it is smaller than the average
    for number in numbers:
        # If the number is smaller than the average, it is added to the new list
        if number < average:
            numbers_smaller_than_avg.append(number)

    return numbers_smaller_than_avg


# Main program
nums = [8, 1000, -3, 0, 2, 5]

nums_total = get_sum(numbers=nums)
print(f"The sum of the numbers in the list is: {nums_total}")
print()

highest_number = get_highest_num(numbers=nums)
print(f"The highest number in the list is: {highest_number}")
print()

lowest_number = get_lowest_num(numbers=nums)
print(f"The lowest number in the list is: {lowest_number}")
print()

numbers_avg = get_average(numbers=nums)
print(f"The average of the numbers in the list is: {numbers_avg}")
print()

numbers_without_middle = get_numbers_mid_removed(numbers=nums)
print(f"The list of numbers with the middle number/s removed is: {numbers_without_middle}")
print()

numbers_sorted_asc = sort_numbers(numbers=nums)
print(f"The list of numbers sorted in ascending order is: {numbers_sorted_asc}")
print()

print_numbers_x_times(numbers=nums, loops=5)
print()

nums_starting_at_index_x = get_numbers_from_x_index(numbers=nums, index=1)
print(f"The list of numbers after the given index position is: {nums_starting_at_index_x}")
print()

numbers_smaller_than_average = print_numbers_smaller_than_avg(numbers=nums)
print(f"The list of numbers smaller than the average of the sum of the original list is: {numbers_smaller_than_average}")
