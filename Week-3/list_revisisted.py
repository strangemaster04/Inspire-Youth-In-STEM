#!/usr/bin/env/python3

#This is a single line comment 
#Python program should illustrate the user of 
#Name :Clive Momanyi
#Email :frankclive024@gmail.com
#Date :17th feb 2023

friends =["masimo","kings","stan","brad"]
print(friends)
friends[0] = "russ"
print(friends)
print("----------------------------------------------")
new_friends = friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)

new_friends.pop()
print(new_friends)
