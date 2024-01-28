# x = [1,2,3,4,5]
# if y:=len(x) > 3:
#     print(y)

# x = []
# for i in range(1,101):
#     if i % 2 == 0:
#         x.append(i)

# print(x)
x = [i for i in range(1,101) if i % 2 == 0]
print(x)
