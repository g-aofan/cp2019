score = float(input("Enter score: "))
if 100>= score>= 70:
    print("A")
elif 70 > score >= 60:
    print("B")
elif 60 > score >= 55:
    print("C")
elif 55 > score >= 50:
    print('D')
elif 50 > score >= 45:
    print('E')
elif 45 > score >= 35:
    print('S')
elif 35 > score >= 0:
    print('U')
else:
    print('Invalid! Score must be within 0 - 100.')
