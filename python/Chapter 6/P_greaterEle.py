
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))

max = 0
if(a>b and a>c and a>d):
    max = a
elif(b>a and b>c and b>d):
    max = b
elif(c>a and c>b and c>d):
    max = c
else:
    max = d

print(max)
