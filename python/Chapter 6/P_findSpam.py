
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe it"
p4 = "click it"

msg = input("Enter your message: ")
if(p1 in msg or p2 in msg or p3 in msg or p4 in msg):
    print("Spam Spam Spam")
else:
    print("Safe Safe")
    