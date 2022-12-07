# Practice 1

age = eval(input("Please enter age:"))
if age > 0:
    if age >= 18:
        print("您可以觀看限制級")
    elif age < 18 and age >= 15:
        print("您可以觀看輔導十五級")
    elif age < 15 and age >= 12:
        print("您可以觀看輔導十二級")
    elif age < 12 and age >= 6:
        print("您可以觀看保護級")
    else :
        print("您可以觀看普遍級")
else:
    print("您輸入0，結束本程式")
        
# Practice 2

name = input("請輸入姓名：")
grade = eval(input("請輸入成績："))
if grade <= 100 and grade >= 90:
    level = "A"
elif grade < 90 and grade >= 80:
    level = "B"
elif grade < 80 and grade >= 70:
    level = "C"
elif grade < 70 and grade >= 60:
    level = "D"
else:
    level = "F"

infile = open("grade.txt","w")
infile.write("************"+"\n")
infile.write("學期成績"+"\n")
infile.write("姓名："+ name+"\n")
infile.write("分數："+str(grade)+"\n")
infile.write("等級："+level+"\n")
infile.write("************"+"\n")

# Practice 3

a,b,c = eval(input("請輸入三角形三邊長(例如:3,4,5):"))
if (a + b) > c and (a + c) >b and (b + c) > a:
    if (a**2) + (b**2) > c**2:
        print("可以構成：","\n","銳角三角形")
    elif (a**2) + (b**2) == c**2:
        print("可以構成：","\n","直角三角形")
    elif (a**2) + (b**2) < c**2:
        print("可以構成：","\n","鈍角三角形")
else:
    print("無法構成三角形")

# Practice 4

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

# Practice 5

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