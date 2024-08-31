my_list = [str(i) for i in range(1, 10)]


print("-" * 13)
for i in range(0, 9, 3):
    print("|", end=" ")
    print(" | ".join(my_list[i:i+3]), end="")
    print(" |")
    if i < 9:
        print("-" * 13)