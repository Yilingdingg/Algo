list=[56,9, 82, 36, 24,1]

def merge_sort(list):
    if len(list)>1:
        mid=len(list)//2
        left=list[0:mid]
        right=list[mid:]
        print(left)
        print(right)
        merge_sort(left)
        merge_sort(right)

    for i in range(1, len(list)):
        temp=list[i]
        j=i-1
        while j>=0 and temp>list[j]:
            list[j+1]=list[j]
            j-=1
        else:
            list[j+1]=temp
    print(list)

merge_sort(list)
        