''' Problem 1. Two Sum Indices'''

def twosum(num,target:int):
    for i in range(len(num)):
        for x in range(i+1,len(num)):
            if num[i]+num[x]==target:
                print([i,x])

twosum([3,11,1,7], 4)
