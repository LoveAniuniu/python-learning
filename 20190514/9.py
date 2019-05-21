# _*_coding:utf-8_*_
#题目：暂停一秒输出。
#程序分析：使用 time 模块的 sleep() 函数。
import time

def jisuan():
    myD = {1:'a', 2:'b'}
    for key, value in dict.items(myD):
        print(key, value)
        time.sleep(1)


if __name__ == "__main__":
    jisuan()