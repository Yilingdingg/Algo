sorted_array=[12,64,98,120,167,192,279,345,715]

low=0
high=len(sorted_array)-1
mid=(low+high)//2

n=int(input("Choose one of the following values in the list:"))
search=False

while low<=high:
    if sorted_array[mid]==n:
        search=True
        print("The number found is the same as the index", n)
        break
    if sorted_array[mid]<n:
        low=mid
    if sorted_array[mid]>n:
        high=mid
    mid=(low+high)//2
if search==False:
    print("The number is not present in the list")
  
print(mid)