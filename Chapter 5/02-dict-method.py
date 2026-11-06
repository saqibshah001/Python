marks={
    "ali": 90,
    "ahmed": 80,
    "sara": 95,
    "youssef": 85
}
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"ali": 100, "saqib": 75}) #ye update wala method update bhi karta hai sath mai add bhi kar deta hai matlab dono ak sath is line mai bhi saqib new add kiya 
print (marks)


# mujhe lagta hai ye dono same kaam kar rahe hain but nahi ye dono alag alag hain .get method ka use kar k hum dictionary me se value ko get karte hain aur agar key exist nahi karti tu ye hume None return kare ga. or ju mene nichy jo step 2 me kiya hai wo ye kaam kare ga k agar key exist nahi karti tu ye error throw kare ga.
# step 1
print (marks.get("ali"))
# step 2
print (marks["ahmed"])



marks.pop("ahmed")
print(marks)



marks.popitem()
print(marks)
