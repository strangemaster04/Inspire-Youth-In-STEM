names = ('clive', 'loreen', 'leon', 'kent', 'paul')

#Accessing items in a list 
print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:3])

#list of fruits
fruits =["apple","mango" ,"cherry" ,"pineapple","passion", "banana", "strawberry"]
print(fruits)
print(fruits[3])
print("my favourite fruit is",fruits [0].upper())

#Adding two list 
vegetables =["kales","cabbage" ,"brocolli" ,"carrots", "spinach"]
stationary =["pens","paper","sharpener","rubber","ruler"]

shoppings =vegetables + stationary 
print(shoppings [5])

#for loop 
for vegetable in vegetables:
    print(vegetable)

for shopping in shoppings:
    print(shopping)
    
print("my name is" + (names[0]) + "and my favourite fruit is" + (fruits[0]))

