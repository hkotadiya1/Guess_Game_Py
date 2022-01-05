# Python program to check validation of password
import re  # import regular expression
while True:
    password = input("Enter valid password: ")
    if re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$", password):
        print("Password is correct!")
        break
    else:
        print("Enter valid password.")
        continue
