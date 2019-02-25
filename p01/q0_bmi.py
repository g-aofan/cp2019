#get input
weight = int(input("Enter weight(kg):"))
height = float(input("Enter height(m):"))
#compute bmi
bmi = weight/(height*height)
#output result
print("bmi={0:.2f}".format(bmi))
if bmi<18.5:
    print("Please eat more")
elif 18.5<=bmi<23:
    print("Low risk")
elif 23<=bmi<27:
    print("Moderate risk")
else:#>=27.5:
    print("High Risk")
    
