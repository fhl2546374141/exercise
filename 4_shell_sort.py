

def shell_sort(alist):
    '''希尔排序'''
    n = len(alist)

    gap = n//2
    # gap变化到0之前，插入算法执行的次数
    while gap > 0:
        # 插入算法与希尔排序的区别是gap的步长
        for j in range(gap,n):
            # j = [gap,gap+1,gap+2,gap+3,...n-1]
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -=gap
                else:
                    break
        # 缩短gap步长
        gap //= 2
if __name__ == '__main__':
    li = [324,424,232,55,334,532,423,444,567,875]
    print(li)
    shell_sort(li)
    print(li)