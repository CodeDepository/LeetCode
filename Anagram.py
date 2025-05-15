from collections import Counter
strs = ["eat","tea","tan","ate","nat","bat"]
hashMap=[]
final=[]
for i,val in enumerate(strs):
    if sorted(val) in hashMap:
        final.append(strs[i])
    
    hashMap.append(sorted(val))

print(hashMap)
print(final)