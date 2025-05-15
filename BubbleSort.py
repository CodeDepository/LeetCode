def bubbleSort( nums : list[int]):
    sorted = True
    while (sorted):
        sorted = False
        list_range = len(nums) - 1
        for i in range(list_range):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                sorted = True
    print(nums)



bubbleSort([2,1,5,7,3])
