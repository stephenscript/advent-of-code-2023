import data
import test_data
import math
import re

nums_dict = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}

def get_end_digits(line):
  left = [math.inf, 0]
  right = [-1, 0]

  # find word versions of nums
  for string, num in nums_dict.items():
    pattern = re.compile(string)
    matches = pattern.finditer(line)

    for match in list(matches):
      index = match.span()[0]
      if index < left[0]:
        left = [index, num]
      if index > right[0]:
        right = [index, num]

  # find digit versions of nums
  for index, char in enumerate(line):
    if char.isdigit():
      if index < left[0]:
        left = [index, int(char)]
      if index > right[0]:
        right = [index, int(char)]
  
  return [left[1], right[1]]

def get_sum(lines):
  sum = 0
  for line in lines:
    left, right = get_end_digits(line)
    sum += int(str(left) + str(right))
  return sum

lines = data.document.split("\n")[1:-1]
test_lines = test_data.test_document.split("\n")[1:-1]
test_lines2 = test_data.test_document2.split("\n")[1:-1]

print("test 1:", get_sum(test_lines))
print("test 2:", get_sum(test_lines2))
print("test 3:", get_sum(['ninetwonine']))
print("result", get_sum(lines))