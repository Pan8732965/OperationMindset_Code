sideLength1,sideLength2,sideLength3 = eval(input("請輸入三角形三邊長(例如:3,4,5):"))
if (sideLength1 + sideLength2) > sideLength3 and (sideLength1 + sideLength3) > sideLength2 and (sideLength2 + sideLength3) > sideLength1:
    print("構成三角形")
else:
    print("無法構成三角形")


