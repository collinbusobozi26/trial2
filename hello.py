# print("Hello world of Code!")
#The Collatz conjecture
def collatz_sequence(n: int) ->list[float]:
    """List of numbers in the collatz sequence starting at n>=0"""

    result = [n]

    while n!=1:
        if n%2==0:
          n = n//2
        else:
           n = 3*n + 1
           result.append(n)

    return result       

print(collatz_sequence(7))

print("The next line is a result of the divisors function")
print("")
#The following lines have been writen directly into the file from Github
def divisors(m:int)-> list[int]:
    """List of all divisors of m, in increasing order."""
    result = []

    for p in range(1, m + 1):
        if m % p == 0:
            result.append(p)

    return result

print(divisors(360))
    
