x = int(input("请输入一个数字: "))
if x > 1:
   for i in range(2,x):
       if (x % i) == 0:
           print(x,"不是质数")
           print(i,"乘于",x//i,"是",x)
           break
   else:
       print("yes")
else:
   print("no")