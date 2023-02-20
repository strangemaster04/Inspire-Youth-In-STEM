n=int(input("1,2,3,4,5,6,7,8,9,10: "))
a=[]
for i in range(0,10):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))