"""
Take two lists, say for example these two:

  list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that
are common between the lists (without duplicates). M
"""
list_a = list(range(1,100,2))
list_b = list(range(1,77,2))
common_list = []

if len(list_b) > len(list_a):
  for x in list_b:
    if x in list_a and x not in common_list:
      common_list.append(x)
else:
  for x in list_a:
    if x in list_b and x not in common_list:
      common_list.append(x)

print(f"list a = {list_a}")
print(f"\nlist_b = {list_b}")

print(f"\ncommon numbers {common_list}")