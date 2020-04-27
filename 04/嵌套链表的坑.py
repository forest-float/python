#!/usr/bin/python3
# @Author: WLP
# @name: 嵌套链表的坑.py
# @date 2020-04-27 11:32

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# scores = [[None] * len(courses)] * len(names)
scores = [[None] * len(courses) for _ in range(len(names))]
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)
# 组合为一个索引序列，同时列出数据下标和数据
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)





