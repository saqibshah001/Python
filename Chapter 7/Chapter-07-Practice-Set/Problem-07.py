n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1))



# Ye Pyramid Star Pattern kehlata hai.
#  Ab har line samjho
# Line 1:   

# n = int(input("Enter the number: "))
# User se number input le rahe hain.

# Maan lo user 5 enter karta hai. To n = 5 ho jayega.

# Line 2:
# for i in range(1, n+1):
# Ye hamara for loop hai.

# Agar n = 5 hai to i ki values hongi:

# 1, 2, 3, 4, 5

# Yani total 5 rows print hongi.

# Line 3:
# # print(" " * (n-i), end="")

# Ye sabse important line hai.

# Ismein hum stars se pehle spaces print kar rahe hain.
# - " " ka matlab ek blank space hai.
# - (n-i) calculate karta hai ke kitne spaces chahiye.
# - end="" ka matlab next print statement ko isi line mein continue karna hai.

# Example:
# i	  Calculation (5-i) 	Spaces
# 1	  5-1	                  4
# 2	  5-2	                  3
# 3	  5-3	                  2
# 4	  5-4	                  1
# 5	  5-5	                  0
# Dekha? Har row mein spaces kam hote ja rahe hain.


# Line 4:
# print("*" * (2*i-1))
# Ye stars print karne ke liye hai.


# Yahan 2*i-1 ka formula use ho raha hai.
# i	Calculation	    Stars
# 1	2×1-1	          1
# 2	2×2-1	          3
# 3	2×3-1	          5
# 4	2×4-1	          7
# 5	2×5-1	          9

# Isliye har row mein 2 additional stars increase ho rahe hain.