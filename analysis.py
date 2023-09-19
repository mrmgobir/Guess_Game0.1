import os


def find_highest_lowest(numbers):
    highest = max(numbers)
    lowest  = min(numbers)
    return highest, lowest

def even_odd_numbers(numbers):
    even_numbers = 0
    odd_numbers= 0
    for num in numbers:
        if num %2 == 0:
            even_numbers += 1
    else:
        odd_numbers += 1
    return even_numbers, odd_numbers

def sum_multiply_numbers(numbers):
    total_sum = sum(numbers)
    final_product = 1
    for num in numbers:
        final_product *= num
    return total_sum, final_product 
