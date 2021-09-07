import math
class BinarySearch():
    # 迭代方式
    def search_iterative(self,list,item):
        low=0
        high=len(list)-1
        while low<=high:
            mid=(low+high)//2
            guess = list[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid-1
            else:
                low=mid+1

        return None
    # 递归方式
    def search_recursive(self,list,low,high,item):
        if high >=low:
            mid=(low+high)//2
            guess = list[mid]
            if guess == item:
                return mid
            elif guess>item:
                return self.search_recursive(list,low,mid-1,item)
            else:
                return self.search_recursive(list,mid+1,high,item)

    def binary_search(self,list,item):
        low = 0
        high =len(list) -1

        while low<= high:
            mid=math.ceil((low+high)/2)
            guess=list[mid]
            if guess == item:
                return mid
            if guess > item:
                high=mid-1
            else:
                low=mid+1
        return None

if __name__ == '__main__':
    bs = BinarySearch()
    my_list = [1,3,5,7,9]
    print(bs.binary_search(my_list,3))
    print(bs.binary_search(my_list,-1))

    print(bs.search_iterative(my_list,3))
    print(bs.search_iterative(my_list,-1))

    print(bs.search_recursive(my_list,0,len(my_list)-1, 3))
    print(bs.search_recursive(my_list,0,len(my_list)-1, -1))
