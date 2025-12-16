# write a program to create email credential if both email and password match print a message welcome to website or enter proper credential

email = "imamnasir73@gmail.com"
password = "Nasir123"

email_in = input("Enter The Email: ")
password_in = input("Enter The Password: ")

if email_in == email:
    if password_in == password:
        print("Welcome to the website")
    else:
        print("Enter proper credential")
else:
    print("Enter proper credential")
