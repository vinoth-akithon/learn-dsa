def duplicates(arr, n): 
    check, result = [], []
    for element in arr:
        if (element in check) and (element not in result):
            result.append(element)
        else:
            check.append(element)

    if result:
        return sorted(result)
    else:
        return [-1]
    
# print(duplicates([0,3,1,2], 4))
print(duplicates([3, 4, 12, 3, 12, 3, 4, 4, 12, 7, 11, 6, 5], 13))
