#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

from nlp05.nlp05 import ngram

if __name__ == '__main__':
    str1 = "paraparaparadise"
    str2 = "paragraph"

    ans1 = set(ngram(str1, 2))
    ans2 = set(ngram(str2, 2))

    waset = ans1 | ans2
    saset = ans1 ^ ans2
    sekiset = ans1 & ans2

    print('和集合', waset)
    print('差集合', saset)
    print('積集合', sekiset)

    if 'se' in ans1:
        print("\"", str1, "\" includes \"se\"")
    else:
        print("\"", str1, "\" doesn't includes \"se\"")
    if 'se' in ans2:
        print("\"", str2, "\" includes \"se\"")
    else:
        print("\"", str2, "\" doesn't includes \"se\"")
