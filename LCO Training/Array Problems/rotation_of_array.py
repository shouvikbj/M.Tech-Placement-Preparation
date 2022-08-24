# Find the number of rotations the array has gone through
# Find the 'Pivot' element to determine the number of rotations the given array has gone through
# Rotation is done on sorted arrays

## Solution can be done using the logic of binary search
## Let the sorted array be => [3,5,8,10,12,16,18,24]
## Let the rotated array be => [12,16,18,24,3,5,8,10]


def find_rotation(arr, low, high):
    if high < low:
        return "NO MATCH"

    # mid = low + ((high - low) // 2)
    mid = int(low + ((high - low) / 2))

    if mid < high and arr[mid + 1] < arr[mid]:
        return mid + 1

    if mid > low and arr[mid] < arr[mid - 1]:
        return mid

    if arr[high] > arr[mid]:
        return find_rotation(arr, low, mid - 1)
    return find_rotation(arr, mid + 1, high)


arr = [12, 16, 18, 24, 3, 5, 8, 10]
low = 0
high = len(arr) - 1

print("Pivot : ", find_rotation(arr, low, high))

arr = [4, 5, 6, 1, 2, 3]
low = 0
high = len(arr) - 1

print("Pivot : ", find_rotation(arr, low, high))
