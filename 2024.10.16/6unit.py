# user_0={
#     'username': 'tom',
#     'first': 'baga',
#     'last': 'laday',
#     }
# # for key,value in user_0.items():
# #     print(key)
# #     print(value)

# user_0['add']='new'
# print(user_0)
# print('\n')
# for k in user_0.keys():
#     print(k,end=" ")

# print('\n')
# for k in sorted(user_0.values()):
#     print(k,end=" ")

# print('\n')
# user_0['new']='new'
# for v in set(sorted(user_0.values())):
#     print(v,end=" ")



####嵌套
alines=[]
aline_temp={'name':'a','color':'red','score':5}
for i in range(50):
    alines.append(aline_temp)

for aline in alines[:5]:
    print(aline)
print("...")    







