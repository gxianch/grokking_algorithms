def sum(list):
    if list==[]:
        return 0
    return list[0]+sum(list[1:])
# 递归实现快速排序 快速排序的性能高度依赖于你选择的基准值。假设你总是将第一个元素用作基准值，且要处理的数组是有序的。
def quicksort(array):
    if len(array) <2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i <=pivot]
        greater=[i for i in array[1:] if i > pivot]
        return quicksort(less)+[pivot]+quicksort(greater)

if __name__ == '__main__':
    print(quicksort([10, 5, 2, 3]))