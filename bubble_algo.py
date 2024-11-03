sorting_array=[87, 0, 1973, -2, 4]

def bubble(sorting_array):
    for i in range(len(sorting_array)):
        for j in range(i,len(sorting_array)):
            if sorting_array[i]>sorting_array[j]:
                #not lost
                sorting_array[i],sorting_array[j]=sorting_array[j],sorting_array[i]
    else:
        return sorting_array

print(bubble(sorting_array))