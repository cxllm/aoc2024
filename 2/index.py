level_lines = []
with open("./input.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        levels = line.split(" ")
        levels = [int(l) for l in levels]
        level_lines.append(levels)

total_safe = 0
count = 0
unsafe = []


def test_safety(levels):
    safe = True
    differences = []
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        differences.append(diff)
    abs_differences = [abs(i) for i in differences]
    if abs(sum(differences)) != sum(abs_differences):
        safe = False
    if abs_differences.count(1) + abs_differences.count(2) + abs_differences.count(
        3
    ) != len(abs_differences):
        safe = False
    return safe


for levels in level_lines:
    safe = test_safety(levels)
    if safe == True:
        total_safe += 1
    else:
        unsafe.append(levels)

additional_safe = 0
for levels in unsafe:
    safe = False
    for i in range(len(levels)):
        temp_levels = [i for i in levels]  # so its a separate instance
        del temp_levels[i]
        safety = test_safety(temp_levels)
        if safety:
            safe = True
    if safe:
        additional_safe += 1

print("Part 1:", total_safe)
print("Part 2:", additional_safe + total_safe)
