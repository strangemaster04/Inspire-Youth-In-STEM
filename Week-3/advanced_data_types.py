#Advanced Data Types 

#Mutable are data types that can change / edited during program life cycle 
#add / remove elements 
#immutable ==> are also data types that cannot be edited during program   

#1 list (mutable )
friends = ["kyle" ,"tate", "peoria","kendall" ]

students = ["ken","mark"]
friends.extend(students)
friends.append("roy")
friends.reverse("bargo")

#2 tuples (imutables)
#type of list that can immune table 
stationaries = ("pens" ,"books" ,"sharpener", "file" ,"stapler")
#replace the whole tuple 
stationaries("ruler" ,"clipboard" , "paperpunch" )
for stationary in stationaries:
    print(stationery)

# Create a dictionary of friends and their hobbies

for friend, hobbies in friend_hobbies.items("swimming"):
    print(f"{friend}'s hobbies are: {', '.join(hobbies)}")


#3 dictionaries AKA dict

#4 sets 

