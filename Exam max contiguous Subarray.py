numbers=list(map(int,input().split()))
maxSum=0
temp=0
for i in range(len(numbers)):
    temp += numbers[i]
    if temp<0:
        temp=0
    elif (maxSum<temp):
        maxSum=temp
print(maxSum)