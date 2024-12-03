import re

text = ""
with open("./input.txt", "r") as file:
    for line in file.readlines():
        text += line

mul_regex = r"mul\([0-9]+,[0-9]+\)"


# Applies to both part 1 and 2
def get_total(text):
    mul_found = []

    for match in re.findall(mul_regex, text):
        mul_found.append(match)
    total = 0
    for mul in mul_found:
        mul = mul.replace("mul(", "").replace(")", "")
        num1, num2 = mul.split(",")
        num1, num2 = int(num1), int(num2)
        total += num1 * num2
    return total


# Part 2 to get rid of sections that don't apply because of don't()
text_without_dont = ""
for split in text.split("do()"):
    without_dont = split.split("don't()")[0]
    text_without_dont += without_dont
print("Part 1:", get_total(text))
print("Part 2:", get_total(text_without_dont))
