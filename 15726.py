a,b,c=list(map(int,input().split()))
x=(a*b/c)
y=(a/b*c)

if(x>y):
    print(int(x))
else:
    print(int(y))
#a b c 에서 a 가 C보다 크면 곱하기 먼저. 아니면 나누기 먼저 

