


X = int(input("請輸入X座標"))

Y = int(input("請輸入Y座標"))

if(X>=0):
   X1=1

if(X<=0):
   X1=3

if(Y>=0):
   Y1=7

if(Y<=0):
   Y1=13

if(X==0):
   X1=23
   
if(Y==0):
   Y1=17

point = X1+Y1

pos = X*X+Y*Y


if(point<=8):
 print("該點在第一象限","離原點距離為根號"+str(pos))
elif(point<=10):
 print("該點在第二象限","離原點距離為根號"+str(pos))
elif(point<=14):
 print("該點在第四象限","離原點距離為根號"+str(pos))
elif(point<=16):
 print("該點在第三象限","離原點距離為根號"+str(pos))
elif(point<=20):
 print("該點在X軸上","離原點距離為根號"+str(pos))
elif(point<=36):
 print("該點在Y軸上","離原點距離為根號"+str(pos))
elif(point<=40):
 print("該點位於原點")