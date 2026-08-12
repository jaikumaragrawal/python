n = int(input("Enter a number till you want the sum of all numbers: "))
sum=0
count = 0
while(count<n+1):
    if count<n+1:
        print(count)
        sum += count
        count +=1
    else:
        break

print("")    
        
print("sum is:", sum)
  