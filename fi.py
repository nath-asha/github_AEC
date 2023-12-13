n = int(input("Enter a number: "))
f, s = 0, 1
print(f, s, end=" ")

for i in range(2, n):
    t = f + s
    print(t, end=" ")
    f, s = s, t