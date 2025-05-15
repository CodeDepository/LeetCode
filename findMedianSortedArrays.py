class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2):
        arr = nums1 + nums2
        arr.sort()
        return self.arrEvenOdd(arr)

    def evenMedian(self,arr):
        mid = len(arr)//2
        return (arr[mid-1] + arr[mid])/2.0

    def oddMedian(self,arr):
        mid = len(arr) // 2
        return arr[mid]

    def arrEvenOdd(self,arr):
        if len(arr) % 2 == 0: 
            return self.evenMedian(arr)
        else: 
            return self.oddMedian(arr)
        


if __name__ == "__main__":
    a = [3, 45, 2]
    b = [5, 6, 4]
    sol = Solution()  
    print(sol.findMedianSortedArrays(a, b))


        
        