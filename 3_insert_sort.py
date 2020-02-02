
# alist = [33,445,7,6,324,536,647,1,34,5]

# 假使 下标为0 的是有序的
# 处理右边的无序元素

# 最坏时间复杂度 为：O(n^2) 最优时间复杂度 为：O(n)  稳定

def insert_sort(alist):
    '''插入排序'''
    n = len(alist)
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1,n):
        # i 表示内层循环的起始值
        i =j
        # 执行从右边的无序序列中取出第一个元素，即i的位置的元素，然后将其插入到右边的有序数列的正确位置
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i -=1
            else:
                break

        # for i in range(j,0,-1):
        #     if alist[i] < alist[i-1]:
        #       alist[i],alist[i-1] = alist[i-1],alist[i]

if __name__ == '__main__':
    li = [33,445,7,6,324,536,647,1,34,5]
    print(li)
    insert_sort(li)
    print(li)
