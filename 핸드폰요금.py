cnt=int(input())
s=list(map(int,input().split()))

y=0
m=0

for i in s:
    y+=(i//30+1)*10
    m+=(i//60+1)*15
if(m==y):
    print("Y M",m)
elif(m>y):
    print("Y",y)
else:
    print("M",m)
