N=int(input())

for i in range(0,N-1):
    print(" "*i+"*"*(2*N-(2*i)-1))
for i in range(0,N):
    print(" "*(N-i-1)+"*"*(2*i+1))