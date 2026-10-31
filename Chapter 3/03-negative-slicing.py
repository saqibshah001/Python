name = "Python"
print(name[-4:-1])

# yaha par index string par depend karta hai. jitny letters ki length hai, utni hi indexing hoti hai. Negative slicing me hum string ke end se start karte hain.

# Negative Slicing 
text = "Computer"
print(text[-5:-2]) #-5 sy value start hoga aur -2 tak print karega. -2 ka matlab hai ky -2 tak print tu hoga but -2 wali value print nahi hogi 

# output:
# put

# C   O   M   P   U   T   E   R
#-8  -7  -6  -5  -4  -3  -2  -1

# Positive Slicing
print(text[2 : 5]) # 2 sy value start hoga aur 5 tak print karega. 5 ka matlab hai ky 5 tak print tu hoga but 5 wali value print nahi hogi

# output:
# mpu 

# C   O   M   P   U   T   E   R
# 0   1   2   3   4   5   6   7
