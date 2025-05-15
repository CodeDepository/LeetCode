def addTwoNumbers(l1, l2):
    Total_l1 = 0
    Total_l2 = 0
    
    for i in range(len(l1)):
        Total_l1 += l1[i] * (10**i)

    for j in range(len(l2)):
        Total_l2 += l2[j] * (10**j)
    
    Sum =  Total_l1 + Total_l2 

    res = list(map(int,str(Sum))) 

    return res   

    
print(addTwoNumbers([1,2,3],[3,5,2]))

