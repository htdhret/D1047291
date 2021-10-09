print("1表示是,0表示否")
x=int(input("是否有房產?"))
if x==1:
    print("可以貸款")
if x==0:
    y=int(input("是否已婚?"))
    if y==1:
        print("可以貸款")
    if y==0:
        z=int(input("是否年收入大於100萬?"))
        if z==1:
            print("可以貸款")
        if z==0:
            print("不能貸款")