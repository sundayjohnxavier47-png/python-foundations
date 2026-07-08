

num = input("Insert number: ")
num = int(num)
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

for i in range(1, num  + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

i = num
while i >= 1:
    print(i, end=" ")
    i -= 1
print()

