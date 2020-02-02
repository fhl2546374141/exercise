

# 最优时间复杂度是：O(nlogn)
# 最坏时间复杂度是：O(n^2)
# 稳定性：不稳定

def quick_sort(alist,first,last):
    '''快排'''
    if first >= last:
        return
    mid = alist[first]
    low = first
    high = last

    while low < high:

        # high左移
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]

        # low 右移
        while low < high and alist[low] <= mid:
            low += 1
        alist[high] = alist[low]

    # 从循环退出时，low == high
    alist[low] = mid

    # 对low左边的列表执行快排
    quick_sort(alist,first,low-1)

    # 对low左边的列表执行快排
    quick_sort(alist,low+1,last)


if __name__ == '__main__':
    li = [324, 424, 232, 55, 334, 532, 423, 444, 567, 875]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)




