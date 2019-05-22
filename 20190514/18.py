#_*_coding:utf-8_*_

#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

#程序分析：关键是计算出每一项的值。
from functools import reduce

def jisuan():
    tn = 0
    sn = []
    n = int(input('请输入:n='))
    a = int(input('请输入:a='))

    for count in range(n):
        tn = tn + a
        a = a * 10
        sn.append(tn)
        print(tn)

    sn = reduce(lambda x,y:x+y,sn)
    print(sn)

if __name__ == "__main__":
    jisuan()