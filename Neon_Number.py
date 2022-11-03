x=int(input())
s=x*x
p=0
while s>0:
    p=p+s%10
    s=s//10
if p==x:
    print("Neon Number")
else:
    print("Not Neon Number")