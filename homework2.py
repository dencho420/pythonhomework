x = int(input())
y = int(input())
a = (x+y)
b = (x*y)
c = (x/y)
d = (x-y)
v = (x//y)
if a>b:
    if a>c:
        if a>d:
            if a>v:
                print(a)
if b>a:
    if b>c:
        if b>d:
            if b>v:
                print(b)
if c>a:
    if c>b:
        if c>d:
            if c>v:
                print(c)
if d>a:
    if d>b:
        if d>c:
            if d>v:
                print(d)
if v>a:
    if v>b:
        if v>c:
            if v>d:
                print(v)


