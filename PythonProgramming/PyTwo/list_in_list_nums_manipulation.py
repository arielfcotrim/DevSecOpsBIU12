# This python script does manipulations to a list of numbers in a list of lists

def get_sum(nums_lists):
    """
    :param nums_lists: A list of lists of numbers.
    :return: total: The sum of the numbers in the list of lists.
    """

    # total variable is initialized to 0 to be incremented later
    total = 0

    # The for loop iterates through each list in the list of lists
    for num_list in nums_lists:
        # The for loop iterates through each number in the list currently being iterated through
        for num in num_list:
            # The number is added to the total variable with each iteration
            total += num

    return total


def get_total_length(nums_lists):
    """
    :param nums_lists: A list of lists of numbers.
    :return: length_of_nums_lists: The length of the list of lists.
    """

    # length_of_nums_lists is initialized to 0 to be incremented later
    length_of_nums_lists = 0

    # The for loop iterates through each list in the list of lists
    for num_list in nums_lists:
        # The length of each list is added to the length_of_nums_lists variable with each iteration
        length_of_nums_lists += len(num_list)

    return length_of_nums_lists


def get_average(total, length):
    """
    :param total: The sum of the numbers in the list of lists.
    :param length: The length of the list of lists.
    :return: average: The average of the numbers in the list of lists.
    """

    average = total / length

    # The average is rounded to 2 decimal places
    rounded_average = round(average, 2)

    return rounded_average


def get_all_numbers(nums_lists):
    """
    :param nums_lists: A list of lists of numbers.
    :return: all_nums: A list of all the numbers in the list of lists.
    """

    # all_nums is initialized to an empty list to be appended to later
    all_nums = []

    # The for loop iterates through each list in the list of lists
    for num_list in nums_lists:
        # The for loop iterates through each number in the list currently being iterated through
        for num in num_list:
            # The number is appended to the all_nums list with each iteration
            all_nums.append(num)

    return all_nums


def get_smallest_num(all_nums):
    """
    :param all_nums: A list of all the numbers in the list of lists.
    :return: smallest_num: The smallest number in the list of lists.
    """

    # smallest_num variable is initialized to the first number in the list since that's the start of the loop
    smallest_num = all_nums[0]

    # The for loop iterates through each number in the list
    for num in all_nums:
        # If the number is less than the smallest_num variable, the number becomes the new smallest_num
        if num < smallest_num:
            smallest_num = num

    return smallest_num


def get_biggest_num(all_nums):
    """
    :param all_nums: A list of all the numbers in the list of lists.
    :return: biggest_num: The biggest number in the list of lists.
    """

    # biggest_num variable is initialized to the first number in the list since that's the start of the loop
    biggest_num = all_nums[0]

    # The for loop iterates through each number in the list
    for num in all_nums:
        # If the number is greater than the biggest_num variable, the number becomes the new biggest_num
        if num > biggest_num:
            biggest_num = num

    return biggest_num


# Main program
new_line = "\n"
lists_of_numbers = [[4, 8, 200], [4, 3000, -1], [5, 87, 12]]

my_total = get_sum(lists_of_numbers)
print("The sum of the numbers in the list of numbers lists is: " + str(my_total) + new_line)

total_length = get_total_length(lists_of_numbers)
my_average = get_average(my_total, total_length)
print("The average of the numbers in the list of numbers lists is: " + str(my_average) + new_line)

smallest_number = get_smallest_num(get_all_numbers(lists_of_numbers))
print("The smallest number in the list of numbers lists is: " + str(smallest_number) + new_line)

biggest_number = get_biggest_num(get_all_numbers(lists_of_numbers))
print("The biggest number in the list of numbers lists is: " + str(biggest_number) + new_line)
