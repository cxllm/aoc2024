# AOC 2024 Day 1 (which I nearly forgot about)
left = []
right = []
# Parsing the input file
with open("./input.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        # the file had a lot of spaces
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

# Part 1
left.sort()
right.sort()
# Nearly forgot this abs function (thank you debugging)
distances = [abs(left[i] - right[i]) for i in range(len(left))]

print("Part 1:", sum(distances))

# Part 2
similarity_score = 0
for item in left:
    similarity_score += item * right.count(item)

print("Part 2:", similarity_score)
