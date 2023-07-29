def find_largest_number(numbers):
    largest_number = None
    for num in numbers:
        if largest_number is None or num > largest_number:
            largest_number = num
    return largest_number


numbers_list = [3, 35, 66, 23, 12]
result = find_largest_number(numbers_list)
print('Biggest number is:', result)


