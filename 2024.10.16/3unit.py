##3.1
# school=['student','teacher','engineer']
# print(school[1].title())
# print(school[-1].title())

##3.2
# #append
# school.append('cook')
# print(school)
# school.append('tress')
# #insert
# school.insert(-1,'cats')
# print(school)
# #del
# del school[2]
# print(school)
# #pop
# sch1=school.pop()
# sch2=school.pop(0)
# print(sch1,sch2)
# print(school)
# #remove
# sch3=school.remove('cook')
# print(sch3)
# print(school)

##3.3 
#使用方法 sort()对列表进行永久性排序
# school=['student','teacher','engineer']
# school.sort()
# print(school)
# school.sort(reverse=True)
# print(school)
#使用函数 sorted()对列表进行临时排序
# school=['student','teacher','engineer']
# print(school)
# print(sorted(school))
# print(school)
#方法reverse()永久性地修改列表元素的排列顺序
school=['student','teacher','engineer']
school.reverse()
print(school)
school.reverse()
print(school)
#使用函数len()可快速获悉列表的长度
print(len(school))

