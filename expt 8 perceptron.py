a=1
w1=0
w2=0
b=0
x1=[1,1,-1,-1]
x2=[1,-1,1,-1]
t=[1,-1,-1,-1]

for j in range (1,3):
    print("epoch:",j)
    for i in range (4):
        yin=x1[i]*w1+x2[i]*w2+b

        if  (yin>0):
            y=1
        elif(yin== 0):
            y=0
        else:
            y=-1
        if(y==t[i]):
            print('x1={},x2={},y={},w1={},w2={},b={}'.format(x1[i],x2[i],y,w1,w2,b))
            continue
        else:
                w1=w1+a*t[i]*x1[i]
                w2=w2+a*t[i]*x2[i]
                b=b+a*t[i]
                print('x1={},x2={},y={},w1={},w2={},b={}'.format(x1[i],x2[i],y,w1,w2,b))
 
