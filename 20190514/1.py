#_*_coding:utf-8_*_

def cf():
    for i in range(1, 10):
        for j in range(1, 1+i):
            print('{}x{}={}\t'.format(i, j, i*j), end='')

def dfh(num1, num2):
    a = num1 % num2
    b = (num1-1) / num2
    return b, a

if __name__ == "__main__":
    cf()
    num2, num1 = dfh(9,4)
    tuple1 = dfh(9, 4)
    print(num1, num2)
    print(tuple1)

    for char in 'liangdianshui':
        print(char)