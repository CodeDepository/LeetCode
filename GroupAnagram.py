from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)

    for i in strs:
        count = [0] * 26
        for j in i:
            count[ord(j) - ord('a')] += 1
            print(count)
        print(count)
        res[tuple(count)].append(i)
        print(res)
    print(res.values())

# or 
def simpleGroupAnagrams(strs):
    res = defaultdict(list)
    for i in strs:
        sorted_i = ''.join(sorted(i))
        print(sorted_i)
        res[sorted_i].append(i)
    print(res)

strs = ["eat","tea","tan","ate","nat","bat"]
# groupAnagrams(strs)
simpleGroupAnagrams(strs)