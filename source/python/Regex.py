import re
# Write a regular expression
# - Input: "Write a Regular Expression"
# - Output: ["W", "R", "E"]

regex = r"[A-Z]"
matched = re.findall(regex, "Write a Regular Expression")
print(matched)