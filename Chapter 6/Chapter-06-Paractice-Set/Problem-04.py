# is problem mai ham apny username ko check karna hai ky wo 10 characters ka hai ya nahi 

username = input("Enter username: ")

if (len(username)<10):
    print("Your username contains less than 10 characters")

else:
    print("Your username is contains more than equal to 10 characters")