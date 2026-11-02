# Append() Method
fruits = ["Apple", "Banana"]
fruits.append("Mango")

print(fruits)

# For Example:
# append() ne list ke end mein Mango add kar diya.


# Insert() Method
Students = ["Ali", "Ahmed", "Ayesha", "Sana"]
Students.insert(1, "Zainab")  # ye index 1 par Zainab ko add kar de ga

print(Students)


# Remove() Method
citys = ["Karachi", "Lahore", "Islamabad", "Quetta"]
citys.remove("Lahore")  # ye Lahore ko list se remove kar de ga
print(citys)


# Pop() Method
cars = ["Toyota", "Honda", "Suzuki", "Kia"]
# cars.pop(1)  # ye index 1 par wali value ko remove kar de ga
print(cars)
cars.pop()  # agar koi index number nahi diya gaya to ye last wali value ko remove kar de ga
print(cars)


# Sort() Method
numbers = [5, 2, 8, 1, 3]
numbers.sort()

print(numbers)

# For Example:
# Numbers chhote se bade order mein aa gaye.

# Reverse() Method
num = [1, 2, 3, 4, 5]
num.reverse()

print(num)