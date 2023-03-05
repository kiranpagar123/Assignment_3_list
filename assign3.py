def sum(numbers):
    total=0
    for i in numbers:
        total += i
    return total
length=int(input("Enter the length: "))
lst=[]
for i in range(length):
    elements=int(input("Enter the elements"))
    lst.append(elements)
result=sum(lst)
print("Sum is: ",result)

#Output:-
#8, 2, 3, 0, 7
#20
