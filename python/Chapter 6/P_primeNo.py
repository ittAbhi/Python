
"""
range(2, n/2) causes an error because n/2 returns a float. Use n//2 or, better, int(n**0.5) + 1.
"""

n = int(input("Enter your number: "))

if n < 2:
    print("It's not prime!")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime!")
            break
    else:
        print("Prime")
