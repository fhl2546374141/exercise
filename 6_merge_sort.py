

# 最优时间复杂度是：O(nlogn)
# 最坏时间复杂度是：O(nlogn)
# 稳定性：稳定

def merge_sort(alist):
    '''归并排序'''
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    # left 采用归并排序后形成的有序的新列表
    left_li = merge_sort(alist[:mid])

    # left 采用归并排序后形成的有序的新列表
    right_li = merge_sort(alist[mid:])


    # 将2个有序列表合并成为一个新列表
    left_pointer,right_pointer = 0,0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer +=1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    li = [324, 424, 232, 55, 334, 532, 423, 444, 567, 875]
    print(li)
    sort_li = merge_sort(li)
    print(sort_li)
