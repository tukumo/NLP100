#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    num = [1, 5, 6, 7, 8, 9, 15, 16, 19, 0]
    for k in range(0, len(num)):
        num[k] -= 1
    ans = []
    for k, v in enumerate(str.split()):
        if k == num[0]:
            num.pop(0)
            ans.append(v[0])
        else:
            ans.append(v[0:2])

    print(ans)