

age = 18
gender ="male"

if (age < 18):
    print("you are still young")
else:
    print("You should get an ID")

#compound / multiple conditions 
if(age > 30) & (gender == "male"):
    print("you qualify for a loan")
else: 
    print("no loan for you")

fav_color = "grey"
age = 22
if(fav_color == "grey") | (age < 20):
    print("Happy birthday to you")
else:
    print("No birthday present to you")
    
