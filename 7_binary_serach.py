
# 最优时间复杂度是：O(1)
# 最坏时间复杂度是：O(logn)

# 递归 二分法查找必须列表是排序好的
def binary_search(alist,item):
    '''二分法查找'''
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True  # 递归退出的条件
        elif item < alist[mid]:
            return binary_search(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:],item)
    return False

# 非递归
def binary_search_2(alist,item):
    '''二分法查找'''
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid-1
        else:
            first = mid+1
    return False



if __name__ == '__main__':
    li = [1, 6, 7, 22, 34, 53, 67, 122, 134]
    print(binary_search(li,34))
    print(binary_search(li,23))
    print(binary_search_2(li,34))
    print(binary_search_2(li,23))



