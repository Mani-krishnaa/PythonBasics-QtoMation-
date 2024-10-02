# break


for i in range(1, 10):
    if i > 5:  # i need one 1 to 5 so we need to break after condition satisfies
        break
    print(i)
print("Programe exited!!!")


# continue
for i in range(1, 11):
    if i ==5:  # i dont need 5 so i will continue
        continue
    print(i)
print("Programe exited!!!")

# continue
for i in range(1, 11):
    if i ==5 or i == 6:  # i dont need 5 and 6 so i will continue
        continue
    print(i)
print("Programe exited!!!")