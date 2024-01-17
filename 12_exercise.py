#make list of number 1 100 only dont print those number who does'nt devided by 3 and 5

# for i in range(1,100):

#     if i/3 and i/5:
        

#     else:
#         print(i)

# i=1

# while i<=100:
#     if i/3 and i/5:
#         i=i+1
#     else:
#         print(i)
#         i=i+1



i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        i = i + 1
    else:
        print(i)
        i = i + 1
