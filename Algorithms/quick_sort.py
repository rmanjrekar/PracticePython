"""
Steps:
1. select any pivot value (can be first, last, middle)
2. compare the items with the pivot
3. Make 2 list, add items greater than pivot in one list and less than pivot in another
4. call quick_sort on both the list with pivot point
   return quick_sort(items_gt_pivot) + [pivot] + quick_sort(items_lt_pivot)
"""

def quick_sort(sequence):
    length = len(sequence)

    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()   # get a pivot element

    items_greater_than_pivot = []
    items_smaller_than_pivot = []

    for i in sequence:
        if i > pivot:
            items_greater_than_pivot.append(i)  # append all elements greater than pivot
        else:
            items_smaller_than_pivot.append(i)  # append all elements smaller than pivot

    return quick_sort(items_smaller_than_pivot) + [pivot] + quick_sort(items_greater_than_pivot)

print(quick_sort([4,5,2,5,7,8,1,9,0,8,10,3,5,6,4]))