data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_data = [data[el] for el in range(1, len(data)) if data[el] > data[el-1]]
# for el in range(1, len(data)):
#     if data[el] > data[el-1]:
#         new_data.append(data[el])
print(new_data)
