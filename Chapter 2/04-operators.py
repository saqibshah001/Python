# Arithmetic Operators
a = 4
b = 7
c = a+b
print(c)

# Assignment Operators

# Examples 1
a = 7-6
print(a)

# Example 2
b = 4
# b += 5    # += is ka matlb ye hai ky b ki value mai  5 add kar du
b -= 1      # -= is matlb ye hai ky b ki value mai sy 1 subract kar du
print(b)


# Comparison Operators
# Is operators ka answer hamesha boolean mai aata hai yahi True ya False

d = 8 > 9
print(d)

f = 7 > 4
print(f)

e = 10<=4  # <= is ka matlb 10 chhota ya 4 ke barabar hai?
print(e)

# < → Sirf chhota
# > → Sirf bara
# <= → Chhota ya barabar
# >= → Bara ya barabar
# == → Barabar hai ya nahi
# != check karta hai ke dono values ek doosre ke barabar hain ya nahi.


# Logical Operators
# and
# Dono conditions True honi chahiye

# Or 
# Kam az kam ek condition True honi chahiye

# Not
# True ko False aur False ko True bana deta hai.

g = True and False
print(g)

h= False or True
print(h)

print(not(True))