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

    