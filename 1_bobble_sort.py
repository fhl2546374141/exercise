

# # 最坏时间复杂度 为：O(n^2) 最优时间复杂度 为：O(n)   稳定

def buble_sort(list):
    '''冒泡排序'''
    n = len(list)
    for j in range(0,n-1):
        count = 0
        for i in range(0,n-1-j):
            if list[i]>list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
        if count == 0:
            return

if __name__ == '__main__':
    li = [11,424,232,55,334,532,423,444,567,875]
    print(li)
    buble_sort(li)
    print(li)

# i 0~n-2  range(0,n-1-0)  j=0
# i 0~n-3  range(0,n-1-1)   j=1
# i 0~n-4  range(0,n-1-2)   j=2
# i 0~n-5  range(0,n-1-3)   j=3
# 总结
#          range(o,n-1-j)


# 最优时间复杂度： O(n)
# 最坏时间复杂度： O(n^2)