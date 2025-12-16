age = int(input("Enter The Age: "))
price = 2000

if age <= 7:
    print("Ticket is Free")
elif age <= 50:
    print("Ticket is", price)
else:
    print("Ticket is", price / 2)
