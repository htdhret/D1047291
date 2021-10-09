x=int(input("年齡"))
if x>30:
    print("不見")
if x<=30:
    y=int(input("長相0:醜，1:帥，2:中等"))
    if y==0:
        print("不見")
    if y==1 or 2:
        z=int(input("收入0:低，1:中，2:高"))
        if z==0:
            print("不見")
        if z==2:
            print("見")
            a=int(input("是否為公務員?0:否，1:是"))
        if a==1:
            a=int(input("見"))
        if a==0:
            a=int(input("不見"))

        