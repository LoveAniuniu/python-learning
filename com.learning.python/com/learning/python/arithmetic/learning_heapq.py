#_*_coding:utf-8_*_
import heapq
#��һ�������л�ȡ������С��N��Ԫ��

if __name__ == "__main__":

    nums = [1,4,6,7,9,7,54,343,232,4,5,6];
    maxnum = heapq.nlargest(5,nums);
    minmun = heapq.nsmallest(2,nums);

    print(maxnum,minmun);
