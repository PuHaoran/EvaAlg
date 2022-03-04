"""
获取当前文件夹下的所有代码，根据一定概率进行随机选择
"""
import os
from random import choice

memory_dict = {
    '快速排序.py': 1,
    '合并集合.py': 1,
    '最短编辑距离.py': 1,
    '编辑距离.py': 1,
    '完全背包问题.py': 1,
    '子矩阵的和.py': 1,
    '数的三次方根.py':1,
}


def main():
    files = [i for i in os.listdir('./') if i.endswith('.py') and i != 'memory_dictionary.py']
    l = []
    for file in files:
        num = 5
        if file in memory_dict:
            num -= memory_dict[file]
        num = max(1, num)
        l += [file] * num
    print(choice(l))


main()
