def rotated_search_helper(arr, low, high, key):
    if low > high:
        return "NO MATCH"

    mid = int(low + ((high - low) / 2))

    if arr[mid] == key:
        return mid

    if arr[low] <= arr[mid] and key <= arr[mid] and key >= arr[low]:
        return rotated_search_helper(arr, low, mid - 1, key)

    elif arr[mid] <= arr[high] and key >= arr[mid] and key <= arr[high]:
        return rotated_search_helper(arr, mid + 1, high, key)

    elif arr[high] <= arr[mid]:
        return rotated_search_helper(arr, mid + 1, high, key)

    elif arr[low] >= arr[mid]:
        return rotated_search_helper(arr, low, mid - 1, key)

    return "NO MATCH"


def rotated_search(arr, key):
    print(f"Index: {rotated_search_helper(arr, 0, len(arr)-1, key)}")


arr = [12, 16, 18, 24, 3, 5, 8, 10]
key1 = 8
key2 = 33
key3 = 12

rotated_search(arr, key1)
rotated_search(arr, key2)
rotated_search(arr, key3)
