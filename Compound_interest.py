p,r,t=map(int,input().split())
a=p*(1+(r/100))**t
form="{:.2f}".format(a)
print(form)