
a = int(input("Enter your age: "))

if(a > 18):
    print("Your are valid!")

elif(a<0):
    print("Invalid age! ")
else:
    print("You are not eligible! ")



# in keyword
l = ["Antu", "Duvya", "kris"]
name = input("Enter name: ")

if(name in l):
    print("Your name is present..")
else:
    print("Sorry@ not here")
