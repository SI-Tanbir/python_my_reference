cars=["audi","bmw","subrau","toyota"]

for i in cars:
    if i == "bmw":
        print(i.upper())

    else:
        print(i.title())

# to check if the value is here we use in
if "toyota" in cars:
    print("its here" )

