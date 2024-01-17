bicycles=["trek","connondal","redline","specialized"]

messages=f"my first my bycle was a {bicycles[0]}"
print(messages)
#.sort() in the list
print(".sort function ")
print(bicycles.sort())


#its add function are like strings .append() but removeing method is deferrent

del bicycles[0] #its remove trek value
print(bicycles)

popped_bicycles=bicycles.pop()
print(bicycles)
print(popped_bicycles)

print(bicycles.pop(0)) #first valu of index
print(bicycles)

# bicycles.remove("redline")

print(bicycles)


car=['bmw','audi','toyota','subaru']
print(car.reverse())
print(car)

like_visit=['maldiv','japan','india','mexico','us','tibat']
print(like_visit)
#useing sort function to reverse value
like_visit.sort(reverse=True)
print(like_visit)