def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j

    nums[i], nums[min_idx] = nums[min_idx], nums[i]

    print(nums)
    return nums


nums = input("Enter the list of numbers to be sorted, separated by spaces: ")
nums = list(map(int, nums.split()))

sorted_nums = selection_sort(nums)
print("The sorted list is:", sorted_nums)
