old_file = []
i = 0

with open('numbers.db', 'r') as file:
    lines = file.readlines()[1:]
# print(first)
print(lines)

with open('numbers.db', 'w') as file:
    file.writelines(lines)
