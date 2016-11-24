#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp30 import mecab_list
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    mecablist = mecab_list('neko.txt.mecab')
    occur = defaultdict(int)
    left = []
    height = []
    total = len(mecablist)

    for v in mecablist:
        occur[v['surface']] += 1

    for k, v in enumerate(sorted(occur.values())):
        left.append(k)
        height.append(v / total)

    for k, v in zip(left, height):
        print(k, v)

    plt.plot(np.array(left), np.array(height))
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
