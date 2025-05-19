"""
Static sliding window
Given a string find the occurence of substring in it.
"""
substr = "test"
string = "testetstestestestst"

def occur_count(string, substr):
    substr_len = len(substr)
    counter = 0
    found_index = []
    for i in range(len(string)):
        start_str = string[i:substr_len]
        if len(start_str) < len(substr):
            break
        if start_str == substr:
            counter += 1
            found_index.append(str(i))
        substr_len += 1
    return f"{substr} found at {','.join(found_index)} of {string}" # to print as a string comma separated
    #return f"{substr} found at {found_index} of {string}"  # to print as list

print(occur_count(string, substr))
