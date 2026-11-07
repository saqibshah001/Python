# is problem mai ham ny apny youtube channel ky liye spam check karny wala function banana hai taky agar koi scammer comment type kary tu show ho jaye 

p1 ="Make a lot of money"
p2 ="buy now"
p3 ="Subscribe this"
p4 ="click this"

message = input("Enter Your Comment: ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not spam")