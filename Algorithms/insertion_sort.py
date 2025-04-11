"""
Steps:
    1. Keep 0th index as a compare item
    2. start the loop from 1st index
    3. compare 0th and 1st element
    4. if 0th is greater than 1st, swap
    5. now check 2nd element with 1st, if 1st is greater than 2nd swap
        then again check the 2nd element with 0th till we sort the front part
"""

def insertion_sort(sequence):

    for i in range(1, len(sequence)):

        # will loop until left item is greater than right and 'i' is greater than 0
        # if any of the above case is false it will exit the loop
        while sequence[i-1] > sequence[i] and i > 0:
            sequence[i-1], sequence[i] = sequence[i], sequence[i-1]
            i -= 1

    return sequence

print(insertion_sort([4,5,2,5,7,8,1,9,0,8,10,3,5,6,4]))