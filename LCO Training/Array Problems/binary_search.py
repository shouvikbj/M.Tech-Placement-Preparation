# Given a sorted array and a value, find it's index

arr = [10, 15, 20, 25, 30, 35, 40, 45, 50]
val1 = 15  # index 1
val2 = 40  # index 6


# recursive approach


def binary_search_helper(arr, val, low, high):
    if low > high:  # corner case handling
        return "NO MATCH"

    mid = low + ((high - low) // 2)

    if arr[mid] == val:
        return mid
    elif val < arr[mid]:
        return binary_search_helper(arr, val, low, mid - 1)
    else:
        return binary_search_helper(arr, val, mid + 1, high)


def binary_search_recursive(arr, val):
    return binary_search_helper(arr, val, 0, len(arr) - 1)


print(binary_search_recursive(arr, val1))
print(binary_search_recursive(arr, val2))


# iterative approach


def binary_search_iterative(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)

        if arr[mid] == val:
            return mid
        elif val < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return "NO MATCH"


print(binary_search_iterative(arr, val1))
print(binary_search_iterative(arr, val2))
