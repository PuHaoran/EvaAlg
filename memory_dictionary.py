"""
获取当前文件夹下的所有代码，根据一定概率进行随机选择
"""
import os
from random import choice

mtl_dict = {
    'ESSM': 1,
    'MMOE': 0,
    'PLE': 0,
}

dl_dict = {
    '损失函数': 0,
    '激活函数': 0,
    '优化算法': 0,
    '过/欠拟合': 0,
    '梯度消失与梯度爆炸': 0,
    'RNN': 1,
    'GRU': 0,
    'LSTM': 1,
    'Softmax和Softmax loss': 0,
    'AUC和gAUC':0,
}

ltr_dict = {
    'LR': 0,
    'GBDT': 0,
    'FM': 0,
    'NCF': 1,
    'Wide&Deep': 0,
    'DIN': 0,
    'BST': 0,
}

memory_dict = {
    '快速排序.py': 1,
    '合并集合.py': 1,
    '最短编辑距离.py': 1,
    '编辑距离.py': 1,
    '完全背包问题.py': 1,
    '子矩阵的和.py': 2,
    '数的三次方根.py': 1,
    '第k个数.py': 1,
    '差分': 1,
}


def choice_kg(dict, item_num=1):
    items = []
    kg_list = []
    for k, v in dict.items():
        items += [k] * max(1, (5-v))
    for _ in range(item_num):
        kg_list.append(choice(items))
    print(kg_list)


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

    choice_kg(dl_dict, 2)
    choice_kg(ltr_dict, 1)
    choice_kg(mtl_dict, 1)


main()
