#_*_coding:utf-8_*_
import heapq
#从一个集合中获取最大的最小的N个元素

if __name__ == "__main__":

    nums = [1,4,6,7,9,7,54,343,232,4,5,6];
    maxnum = heapq.nlargest(5,nums);
    minmun = heapq.nsmallest(2,nums);

    print(maxnum,minmun);
