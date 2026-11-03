# ye count()  Method value ka bata hai ky hamary tuple mai ak value kitni bar use hoi hai
a = (1,32,44,32,34323,False, " haider" ,21)

# step 1
no = a.count(32)
print(no)

# step 2
print(a.count(1))  # ye 1 value ka count bata de ga

# step 1 or 2 dono same hi hain but step 1 mai pehlay variable mai store kar ke print kiya aur step 2 mai direct print kiya.


# index Method 
# index method value ka index bata hai ky hamary tuple mai ak value kis index par hai.

index_no = a.index(False)
print(index_no)