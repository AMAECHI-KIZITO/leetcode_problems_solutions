''' Index of the First Occurrence in a String'''

def first_occurence(haystack:str, needle:str):
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
    


