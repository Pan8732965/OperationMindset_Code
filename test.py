try:
    #兩點距離
    import math
    x1,y1,z1 = eval(input("請輸入第一個座標x,y,z:"))
    x2,y2,z2 = eval(input("請輸入第二個座標x,y,z:"))
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    r = distance / 2
    print("兩點間的距離：",round(distance,4))
    #圓面積
    area = math.pi*r*r
    print("面積:",round(area,2))
    if area >= 100:
        print("為大圓")
    elif area < 100:
        print("為小圓")
except:
    print("輸入錯誤！程式結束！")