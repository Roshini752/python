n=7
m=21

for i in range(1,n+1):
    if i<=n//2:
        c=".|." * (2*i-1)
        print(c.center(m,'-'))
    elif i==((n//2)+1):
        d="WELCOME"
        print(d.center(m,'-'))
    else:
        j=n-i
        c=".|." * (2*j+1)
        print(c.center(m,'-'))
