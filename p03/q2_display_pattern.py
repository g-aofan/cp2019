n = int(input("Enter n: "))
for row in range(1, n+1):
    #print decreasing number of space
    print(' '*(n-row), end="")
    #print increasing number of digits
    for col in range(row,0,-1):
        print(col,end ="")
    print()
