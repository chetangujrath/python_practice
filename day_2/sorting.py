"""""
bubble sort algorithm implementation in Python. This algorithm repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The process is repeated until the list is sorted.
"""



list_of_nums = [1, 2, -5, 3, 3, -3, 2, 2, -2, 1, -4, 5, 65, 2, -3, -6, -9, 10]
print("Before sorting:", list_of_nums)  # This will print the original list

for i in range(len(list_of_nums)):
    for j in range(len(list_of_nums)):
        if list_of_nums[i] > list_of_nums[j]:
            # Swap the elements
            temp = list_of_nums[i]
            list_of_nums[i] = list_of_nums[j]
            list_of_nums[j] = temp
    
print("after sort",list_of_nums)  # This will print the list after each pass of the outer loop






#list_of_nums.sort()  # This will sort the list in place
#print("After sorting:", list_of_nums)  # This will print the sorted list