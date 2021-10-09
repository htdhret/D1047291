x= int(input("输入一个年份:"))
if (x % 4) == 0:
   if (x % 100) == 0:
       if (x % 400) == 0:
           print("{0} 是闰年".format(x))  
       else:
           print("{0} 平年".format(x))
           print(x%400+x)
   else:
       print("{0} 是闰年".format(x))       
else:
   print("{0} 平年".format(x))