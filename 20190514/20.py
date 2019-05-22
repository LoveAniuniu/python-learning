#_*_coding:utf-8_*_
#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

#程序分析：无

def jisuan():
    tour = []
    height = []

    hei = 100.0
    tim = 10

    for i in range(1, tim + 1):
        if i == 1:
            tour.append(hei)
        else:
            tour.append(hei*2)

        hei /=2
        height.append(hei)
    
    print('tour={0}'.format(sum(tour)))
    print('height={0}'.format(height[-1]))

if __name__ == "__main__":
    jisuan()