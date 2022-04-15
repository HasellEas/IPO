nums = {'hello': 2, 'hi': 1, 'who': 3, 'where': 1, 'why': 1}
out = {}
list_d = list(nums.items())
list_d.sort(key=lambda i: i[1])
list_d.reverse()
for i in list_d:
    out.update({i[0]:i[1]})
print(out)