sorting_array=[7,35,-1,0,209]

for i in range(len(sorting_array)):
    for j in range(i,len(sorting_array)):
        if sorting_array[i]>sorting_array[j]:
            #not lost
            sorting_array[i],sorting_array[j]=sorting_array[j],sorting_array[i]


print(sorting_array)