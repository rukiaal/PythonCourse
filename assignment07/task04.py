def remove_odd(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

nums = [1, 2, 3, 4, 5, 6]
filtered = remove_odd(nums)

print("Original list:", nums)
print("Even numbers only:", filtered)
