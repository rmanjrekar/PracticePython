"""
Always on sorted array
Steps:
    1. set 0th index as a start point
    2. calculate jump size : jump_size = sqrt(length of input sequence)
    3. loop through entire sequence by checking item to be searched
    4. check if item > nums[current]
        if yes, current = current + jump_size, jump on that index
        and then check step 4 again
        if no, then check the items in the reverse order till previous current index(current-jump_size) or find the item
"""

def jump_search(nums, to_search):
    length = len(nums)
    jump_size = round(length**0.5)
    current = 0
    count = 0
    while count < length:
        if to_search == nums[current]:
            return f"Found at index {current}"
        elif to_search > nums[current]:
            if current + jump_size >= length-1:
                current = length-1
            else:
                current += jump_size
        else:
            i = current - 1
            while i > current-jump_size:
                if nums[i] == to_search:
                    return f"Found at index {i}"
                i -= 1
        count += 1
    return "Not found"

print("Output--->" , jump_search([2,3,4,5,6,7,8,9,10,11],2))


#################################Another way#############################################################
"""
Steps:
    1. set 0th index as a start point
    2. calculate jump size : jump_size = sqrt(length of input sequence)
    3. get the current_index to do reverse linear search by comparing with the item_to_search
    4. reverse linear search from current_index till prev jump index (current_index-jump_size)
"""

def another_way(seq, item_to_search):
    length = len(seq)
    current_index = 0

    jump_size = round(length**0.5)

    #### to get the index from where we can do reverse linear search
    while seq[current_index] < item_to_search:
        if current_index + jump_size > length:
            current_index = length-1
            break
        else:
            current_index += jump_size

    #### reverse linear search till the previous jump index which can be calculated using current-jump_size
    for i in range(current_index,current_index-jump_size,-1):
        if seq[i] == item_to_search:
            return f"Item found at {i}"

    return "Not found"

print("Output--->" , another_way([2,3,4,5,6,7,8,9,10,11],4))