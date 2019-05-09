#_*_coding:utf-8_*_
# 解压赋值

#基本用法
def baseFun():
    data = ['wanghao',50,(19,29)];
    name,age,date=data
    print(name,age,date)

def recordFun():
    data = ['wanghao',20, '3333','4444']
    name,age,*numb=data
    print(name,age,numb)

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

def do_records():
    records = [ ('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4), ]

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

if __name__ == "__main__":
    do_records()