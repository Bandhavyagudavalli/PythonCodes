n=int(input())
sum=0
while (n>0):
    temp=n%10
    sum+=temp
    n//=10
    
print(sum)

def sum(n):

    return(n*(n+1)//2)

print(sum(5))