# in for else break must be used
# loop will come to else part when all the iteration is completed

nums=[22,3,44,6,7]

for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("not found")