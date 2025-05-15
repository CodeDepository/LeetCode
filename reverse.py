class Solution:
    def reverse(self, x) :
        arr = list(map(int, str(x)))
        arr.reverse()
        
        number = 0
        for num in arr:
            number = number*10 + num
        return number
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))