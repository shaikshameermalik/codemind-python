x,y=map(int,input().split())
sum=x+(2*y)
if x==0 and y%2==0:
    print("YES")
elif x==0 and y%2!=0:
    print("NO")
elif sum%2==0:
    print("YES")
else:
    print("NO")