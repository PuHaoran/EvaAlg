"""
获取当前文件夹下的所有代码，根据一定概率进行随机选择。
"""
import os
from random import choice


mtl_dict = {
    'ESSM': 1,
    'MMOE': 3,
    'PLE': 2,
    'MMOE_Transformer': 2,
}

dl_dict = {
    '损失函数': 3,
    '激活函数': 1,
    '优化算法': 0,
    '过/欠拟合': 2,
    '梯度消失与梯度爆炸': 3,
    'RNN': 3,
    'GRU': 0,
    'LSTM': 2,
    'Softmax和Softmax loss': 0,
    'AUC和gAUC':2,
    'Word2vec': 0,
    'session划分': 0,
    'pltv预估': 0,
}

ltr_dict = {
    'LR': 2,
    'GBDT': 0,
    'NCF': 1,
    'FM': 2,
    'NFM': 0,
    'AFM': 1,
    'Wide&Deep': 0,
    'DeepFM': 0,
    'DIN': 1,
    'BST': 1,
    'bandit': 0,
}

memory_dict = {
    '快速排序.py': 1,
    '合并集合.py': 2,
    '最短编辑距离.py': 1,
    '编辑距离.py': 1,
    '完全背包问题.py': 1,
    '子矩阵的和.py': 2,
    '数的三次方根.py': 1,
    '第k个数.py': 1,
    '差分.py': 1,
    '模拟队列.py': 1,
    '八数码.py': 1,
    '滑动窗口.py': 1,
    'n皇后问题.py': 1,
    '二进制中1的个数.py': 1,
    '剑指 Offer 04. 二维数组中的查找.py': 1,
    '剑指 Offer 05. 替换空格.py': 1,
    '剑指 Offer 12. 矩阵中的路径.py': 1,
    '剑指 Offer 22. 链表中倒数第k个节点.py': 1,
    '数组元素的目标和.py': 1,
    '剑指 Offer 29. 顺时针打印矩阵.py': 1,
    '剑指 Offer 31. 栈的压入、弹出序列.py': 1,
    '剑指 Offer 47. 礼物的最大价值': 1,
    '剑指 Offer 57. 和为s的两个数字.py': 1,
    '剑指 Offer 58 - I. 翻转单词顺序': 1,
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
    files = [i for i in os.listdir('./') if i.endswith('.py') and i != 'memory_dictionary.py' and i != 'beta0.1.py']
    files += [i for i in os.listdir('./剑指offer/') if i.endswith('.py')]
    l = []
    for file in files:
        num = 5
        if file in memory_dict:
            num -= memory_dict[file]
        num = max(1, num)
        l += [file] * num
    print(choice(l))
    print(choice(l))
    choice_kg(dl_dict, 1)
    choice_kg(ltr_dict, 1)
    choice_kg(mtl_dict, 1)


main()
