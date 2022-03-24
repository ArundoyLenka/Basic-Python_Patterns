#star_pattern printing

n = int(input("Enter the number of stars you want to print: "))

option = int(input("Type 1 or 0: "))
new = bool(option)

if new == True:
    for i in range(1, n+1):
        print("*"*int(i))

elif new == False:
    for i in range(n, 0, -1):
        print("*"*int(i))
