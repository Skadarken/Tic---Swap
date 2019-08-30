a = [85, 45, 76, 79, 81]
count = len(a)
print(a)
for i in range(count):
    for k in range(i, count):
        if(a[i] > a[k]):
            a[i],a[k] = a[k],a[i]

print("Sorted a =", a)