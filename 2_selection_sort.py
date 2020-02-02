
# alist = [44,55,65,66,33,23,58,99]
# 下标      0  1  2  3  4  5  6  7

# j=0  i(0+1,n)
# 开始就定义 下标为0的最小 min=0
# 开始遍历列表 与min 进行比较 min = 5

# alist[0],alist[5] = alist[5],alist[0]
# alist = [23,55,65,66,33,44,58,99] 此为交换一次的结果 最小值放到最前边

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# j=1 i(1+1,n)
# 开始就定义 下标为1的最小 min=1
# 开始遍历列表 与min 进行比较 min = 4

# alist[1],alist[4] = alist[4],alist[1]
# alist = [23,33,65,66,55,44,58,99] 此为交换2次的结果 最小值放到最前边

# ........
# 一次类推
# j=n-1 i(1+j,n)
# alist = [23,33,44,55,58,65,66,99]

# 最坏时间复杂度 为：O(n^2) 最优时间复杂度 为：O(n^2)  不稳定

def select_sort(alist):
    '''选择排序'''
    n = len(alist)
    for j in range(0,n-1):
        min_index = j
        for i in range(1+j, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]

if __name__ == '__main__':
    li = [44, 55, 65, 66, 33, 23, 58, 99]
    print(li)
    select_sort(li)
    print(li)









