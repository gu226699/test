#4.3.2
# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))
# print((squares))

#列表解析
# squares=[i**2 for i in range(1,6)]
# print(squares)
# line=[i*2+1 for i in range(0,11)]
# print(line)

#复制列表（1.切片复制 2.创建副本（关联））
mylist=[1,2,3,4,'xb']
hislist=mylist[:]
print(hislist)
mylist.append('new_element')
hislist.append('another_element')
print(mylist)
print(hislist)

mylist=[1,2,3,4,'xb']
hislist=mylist
print(hislist)
mylist.append('new_element')
print(mylist)
print(hislist)