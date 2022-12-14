total = 0
total_list = []
original_info = open("day1.txt", "r")

for x in original_info:
  if x != "\n":
    num = int(x)
    total = num + total
  if x == "\n":
    total_list.append(total)
    total = 0

print(max(total_list))
new_total_list = sorted(total_list)
total_of_top_three_elves = new_total_list[-1] + new_total_list[-2] + new_total_list[-3]
print(total_of_top_three_elves)