from re import L


N=int(input())

for i in range(0,N):
    print("*"*(i+1)+" "*((N-(i+1))*2)+"*"*(i+1))
for i in range(0,N-1):
    print("*"*(N-(i+1))+" "*((i+1)*2)+"*"*(N-(i+1)))
