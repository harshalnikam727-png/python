a=int(input("enter the number:  "))
if (a<0):
    print("number is negative")
elif (a==0):
    print("number is zero")
else:
    print("number is positive")
print("i am happy now")

# mini challenge from ai
c=int(input("enter the number:  "))
if(c<=100 and c>=90):
    print("A")
elif(c<90 and c>=80):
    print("B")
elif(c<80 and c>=70):
    print("C")
elif(c<=70 and c>=0):
    print("fail")
else:
    print("invalid input")
print("challenge completed")

x=int(input("enter the number  "))
match x:
    case 0:
        print("the number is zero")
    case _ if(x<0):
        print("number is negative")
    
    case 7:
        print("thala for a reason")
    case _ :
        print("number is positive")
y=int(input("enter the year:  "))
if(y%100!=0 and y%4==0):
    print("leap year")
elif(y%100==0 and y%400==0):
    print("leap year")
elif(y%100==0 and y%400!=0):
    print("non leap year")
else:
    print("non leap year")
a=("harshal anilkumar nikam")
for i in a:
    print(i,end=" ")
for h in range(7):
    print(h)
for k in range(2,27,3):
    print(k)
c=["red","blue","green","orange"]
for x in c:
    print(x)
    for y in x:
        print(y)
for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5*",i,"=",5*i)
n=int(input("enter any positive number:  "))
for i in range(1,1+n):
    if(i%3==0):
        continue
    if(i%10==5):
        continue
    print(i)
def avg(a,b):
    avg=(a+b)/2
    print(avg)
def less(a,b):
    if(a>=b):
        print("first number is greater")
    else:
        print("second number is greater")
a=int(input( ))
b=int(input( ))
avg(a , b)
less(a,b)
c=int (input ())
d=int ( input ())
avg(c,d)
less(c,d)
