friends = ["Apple", "Orange", 5, 325.21, True, "Ali"]
print(friends[0])

# agar mujhe list mai changing karni hogi mai is tarha karo ga is mai mene index 0 wali jaga par 
friends[0] = "Banana"
print(friends[0])

# string mai eysa hota tha ky ham koi bhi function lagaty thy apny string mai tu wo ak new string us function sy bani hoi hamy dy deta tha but is list mai eysa nahi hota wo direct new string nahi banata wo direct apny list mai hi changing kar deta hai

print(friends[0])
print(friends[1:3])  # ye slice kar raha hai index 1 sy 3 tak ka data print kare ga but 3 ko include nahi kare ga