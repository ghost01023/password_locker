from random import sample
# import antigravity
from math import ceil

print(b'2005-05-26-10458.68')

# binary_data = bytes([])
# print(binary_data.decode("utf-16"))
val = []
for x in [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]:
    val.append(x.to_bytes(length=4, byteorder="little", signed=False))

for value in val:
    print(value.decode("utf-32"), end="")
print()
nums = [10, 10, 10, 10]
min_num = None

while len(nums):
    min_num = min(nums)
    if min_num < 10 and min_num:
        nums.remove(min_num)
    else:
        break

# if min_num:
#     print(min_num)

set1 = {1, 88}
set2 = {1, 89}


# for val in set1.union(set2):
#     print(val)


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ["Maths", "Art", "SST", "English", "Psychology", "Diuresticalllogy", "Dermatologistics"]
into = {"name": "John", "age": 45}
# student_info(*courses, **into)

arr = []
for i in range(1000):
    arr.extend(sample(courses, 2))

size = len(sorted(courses, key=lambda y: len(y))[-1])
size += 4 - (size % 4)
print(size)

dic = dict()

for val in arr:
    dic[val] = 1 if val not in dic.keys() else dic[val] + 1

dic = sorted(dic.items(), key=lambda y: y[1])
for keys, values in dic:
    left_tabs = int(ceil((size - len(keys)) / 4))
    print(keys + ("\t" * left_tabs) + str(values))
