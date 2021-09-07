"""scr = open('scores.csv')
task = open('task.csv', 'a+')
for std in scr:
    std = std.split(',')
    scores = [int(i) for i in std[1::]]
    ave = sum(scores) / (len(scores))
    task.write(f'{std[0]},{ave}\n')
dic = {}
for std in scr:
    std = std.split(',')
    scores = [int(i) for i in std[1::]]
    ave = sum(scores) / (len(scores))
    dic[ave] = std[0]
for i in sorted(dic):
        task.write(f'{dic[i]},{i}\n')"""

from heapq import nlargest
from heapq import nsmallest


def func(item):
    return item[1]


scr = open('scores.csv')
task = open('task.csv', 'a+')
dic = {}
task.write('task1\n')
for std in scr:
    std = std.split(',')
    scores = [int(i) for i in std[1::]]
    ave = sum(scores) / (len(scores))
    task.write(f'{std[0]},{ave}\n')
    dic[std[0]] = ave

task.write('\ntask2\n')
for key, value in sorted(dic.items(), key=func):
    task.write(f'{key},{value}\n')

task.write('\ntask3\n')
top3 = nlargest(3, dic, key=dic.get)
for std in top3:
    task.write(f'{std},{dic.get(std)}\n')

task.write('\ntask4\n')
low3 = nsmallest(3, dic, key=dic.get)
for std in low3:
    task.write(f'{dic.get(std)}\n')

task.write('\ntask5\n')
task.write(f'{sum(dic.values()) / len(dic)}')