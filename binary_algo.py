sorted_array=[92, 65,100,-57,-7,129,405,31,73,118]
sorted_array.sort()

n=int(input("Choose one of the following values in the list:"))

def Binary_search(sorted_array,n):
    low=0
    high=len(sorted_array)-1
    search=False
    while low<=high:
        mid=(low+high)//2
        if sorted_array[mid]==n:
            search=True
            print("The number found is", n, "at index",mid)
            break
        elif sorted_array[mid]<n:
            low=mid+1
        elif sorted_array[mid]>n:
            high=mid-1
    if search==False:
        print("The number is not present in the list")

print(Binary_search(sorted_array,n))