print("{0:10}{1:20}{2:10}   {3}".format("Miles","Kilometres","Kilometres","Miles"))
for i in range (1,11):
    print("{0:<10}{1:<20}{2:<10}   {3:<}".format(i,"{0:.3f}".format(i*1.609),i*5+15,"{0:.3f}".format((i*5+15)/1.609)))
