# agar mujhe set mai or vlaue add karna ho to mai add method ka use karunga
set1 = {1, 2, 3, 4, 5}
set1.add(6)
print(set1)

set1.remove(3)
print(set1)



s = {1, 2, 3}

s.update([4, 5, 6])

print(s)



s = {1, 2, 3, 4, 5}

s.discard(3)

print(s)




s = {1, 2, 3, 4, 5}

s.pop()

print(s)




s = {1, 2, 3, 4, 5}

s.clear()

print(s)




s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))



s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1.intersection(s2))




s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1.difference(s2))