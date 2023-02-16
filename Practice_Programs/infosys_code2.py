n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

k = int(input())

x = a[k]
a[k] = a[0]
a[0] = x
print(a)