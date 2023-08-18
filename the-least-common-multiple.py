def functioon(a, b):
    s = []
    for i in range(1, a+1):
        if a % i == 0:
            s.append(i)
            x = []
            for v in s:
                if b % v == 0:
                    x.append(v)
                    y = max(x)
    return y * (a/y) * (b/y)


while True:
    print("Press 'w' two times to exit")
    k = input("Enter the first number:")
    q = input("Enter the second number:")
    if k != "w" and q != "w":
        k = int(k)
        q = int(q)
        print("the least common multiple is :", functioon(k, q))

