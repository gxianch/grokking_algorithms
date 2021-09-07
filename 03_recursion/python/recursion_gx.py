def countdown(i):
    if i<=0:
        return 0
    else:
        print(i)
        return countdown(i-1)

def greet2(name):
    print("how are you, ",name,"?")
def bye():
    print("ok bye!")
def greet(name):
    print("how are you, ", name, "?")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def binary_search(arr,target):
    if not arr:
        return -1
    if len(arr) == 1 and arr[0]==target:
        return arr[0]
    if len(arr) ==1 and arr[0]!=target:
        return -1
    low =0
    high=len(arr)-1
    mid=(low+high)//2
    if arr[mid]> target:
        return  binary_search(arr[:mid],target)
    else:
        return binary_search(arr[mid+1:],target)
# 递归求数组最大值
def find_max(arr):
    if len(arr)==2:
        return  arr[0] if arr[0] > arr[1] else arr[1]
    sub_max=find_max(arr[1:])
    return  arr[0] if arr[0] > sub_max else sub_max
# 递归求数组之和
def sum_arr(arr):
    if not arr:
        return 0
    return arr[0]+sum_arr(arr[1:])
if __name__ == '__main__':
    countdown(10)
    greet("adit")
    list=[5,4,6,2,10]
    print(binary_search(list,4))
    print(find_max(list))
    print(sum_arr(list))