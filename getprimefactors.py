#calculating how many prime factors in a given number

dividers=[]
primes=[]

n=int(input("What is the number? "))
firstn=n

#find dividers of given number

for i in range(2,n+1):
    if n%i==0:
        dividers.append(i)

#find prime factors of given number

for x in dividers:
    for t in range(2,x):
        if x%t==0:
            break
    else:
        primes.append(x)

#find how many prime factors in given number        
count=0
primefactors={} #you can make a dictionary of prime factors and how many of prime factors
primescount=[]

#find how many prime factors

for i in range(len(primes)):
    count=0
    while n%primes[i]==0:
        
        count+=1
        n=n/primes[i]
        primefactors[primes[i]]=count #you can add prime factors and how many of prime factors to a dict
    primescount.append(count)

#print the output
print(f"{firstn}'s prime factors are:",end=" " )
for i in range(len(primes)):
    print(f"{primes[i]}^{primescount[i]}",end=" ")#print output as primefactor^primefactorcount
    