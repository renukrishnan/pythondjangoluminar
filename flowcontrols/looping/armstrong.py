# 123= 1*1*1+2*2*2+3*3*3=36  this program is called as armstrong
num=int(input("enter a number:"))
res=0
while(num>0):
    digit=num%10
    res=res+digit**3
    num=num//10
print(res)