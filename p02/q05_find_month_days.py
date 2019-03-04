month = int(input('Enter Month: '))
year = int(input('Enter Year: '))
months = ["January", "February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
n = months[month-1]
t_d = [4,6,9,11]
t_o_d =[1,3,5,7,8,10,12]

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month == 2:
    print(n,"in",year,"has 29 days.")
elif month == 2:
    print(n,"in",year,"has 28 days.")
elif month in t_d:
    print( n,"in", year,"has 30 days.")
elif month in t_o_d:
    print(n,"in",year,"has 31 days.")
