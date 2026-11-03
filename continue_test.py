print("=== break ===")
for i in [1,2,3,4]:
    if i == 3:
        break
    print(i)

print("=== continue ===")
for i in [1,2,3,4]:
    if i == 3:
        continue
    print(i)

print("=== 不加 ===")
for i in [1,2,3,4]:
    print(i)