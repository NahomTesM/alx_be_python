num = int(input("Enter the size of the pattern: "))
count = 1
while count <= num:
    for number in range(1,num+1):
        print("*", end="")
    print()
    count = count + 1
