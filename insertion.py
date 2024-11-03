list=[23,1, 10, 5, 2]

for i in range(1, len(list)):
    temp=list[i]
    j=i-1
    while j>=0 and temp<list[j]:
        list[j+1]=list[j]
        j-=1
    else:
        list[j+1]=temp

print(list) 