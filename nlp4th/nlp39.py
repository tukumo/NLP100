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

    for k, v in enumerate(sorted(occur.values(), reverse=True)):
        left.append(k)
        height.append(v / total)

    plt.plot(np.array(left), np.array(height))
    plt.xscale('log')
    plt.yscale('log')
    plt.title('nlp39.py')
    plt.xlabel('出現頻度順位')
    plt.ylabel('出現頻度')
    plt.show()
