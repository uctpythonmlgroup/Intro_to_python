a=1
b=1
for k in range(0,9):
    print(min(a,b))
    print(max(a,b))
    b = a + b
    a=b+a
