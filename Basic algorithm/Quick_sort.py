# coding = utf-8


# 快排主函数
def quick_sort(l, left, right):
    if left>=right:
        return
    index = part_sort(l, left, right)
    # 递归
    quick_sort(l, left, index-1)
    quick_sort(l, index+1, right)
    
    
def part_sort(l, left, right):
    start = left  # 枢纽值的序号
    key = l[left]  # 枢纽值
    while(left<right):
        while(left<right and key<=l[right]):
            right -= 1
        while(left<right and key>=l[left]):
            left += 1
        l[left], l[right] = l[right], l[left]
    l[start], l[left] = l[left], l[start]
    return left
    
    
    
if __name__ == "__main__":
    l = [6,1,2,7,9,3,4,5,10,8]
    quick_sort(l, 0, len(l)-1)
    print(l)
