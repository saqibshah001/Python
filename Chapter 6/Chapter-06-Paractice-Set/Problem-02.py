# is problem mai ham ny us ky sary subject ky marks ly kar jus ko show karwana hai ky tumhari percentage kitni hai or tum pass hu ya nahi 

marks1 =int(input("Enter Marks 1: "))
marks2 =int(input("Enter Marks 2: "))
marks3 =int(input("Enter Marks 3: "))

# Check Percentage 

total_percentage=(100*(marks1 + marks2 +marks3))/300

if (total_percentage >= 40 and  marks1>=33  and marks2>=33  and marks3>=33):  
    print("You are PASS", total_percentage)
else:
    print("You are FAIL", total_percentage)