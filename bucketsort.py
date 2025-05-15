from collections import defaultdict

def topKFrequent(nums, k):
    #Get the frequecy the element is appearing in the array
    freq_map = defaultdict(int)
    bucket = [[] for i in range(len(nums)+1)] #bucket: index will be the counts that element is appearing the the values in that list single or multiple are which element is appearing that many time

    #Adding values in hash
    for i in nums:
        freq_map[i] += 1
    
    # adding values in bucket list from the hashmap
    for index, count in freq_map.items():
        bucket[count].append(index)
    
    # printing the top k most appearing elements
    result = [] # it could be multiple elements so we created a list to simple add in this then printing those
    for freq in range(len(bucket)-1,0,-1):
        for num in bucket[freq]:
            result.append(num)
            if len(result)==k:
                return result




topKFrequent([1,2,1,4,2,2,5],2)