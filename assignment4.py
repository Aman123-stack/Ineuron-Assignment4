q1>def arraysIntersection(arr1, arr2, arr3):
    result = []
    i, j, k = 0, 0, 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return result

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
result = arraysIntersection(arr1, arr2, arr3)
print(result)
q2>def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    result = [list(set1 - set2), list(set2 - set1)]
    return result

# Example usage
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDisappearedNumbers(nums1, nums2)
print(result)
q3>def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with swapped dimensions
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose(matrix)
print(result)

q4>def arrayPairSum(nums):
    nums.sort()  # Sort the array in ascending order
    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum

# Example usage
nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
print(result)
q4>def arrangeCoins(n):
    left = 0
    right = n

    while left <= right:
        mid = left + (right - left) // 2
        coins_needed = (mid * (mid + 1)) // 2

        if coins_needed == n:
            return mid  # Found exact number of coins, return number of rows
        elif coins_needed < n:
            left = mid + 1  # Increase number of rows
        else:
            right = mid - 1  # Decrease number of rows

    return right  # Return number of rows with complete coins

# Example usage
n = 5
result = arrangeCoins(n)
print(result)
q5>def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1

    return result

# Example usage
nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)
q6>def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1

    return result

# Example usage
nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)
q7>def maxCount(m, n, ops):
    min_row = m
    min_col = n

    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])

    return min_row * min_col

# Example usage
m = 3
n = 3
ops = [[2, 2], [3, 3]]
result = maxCount(m, n, ops)
print(result)
q8>def shuffle(nums, n):
    result = []

    i, j = 0, n

    while i < n:
        result.append(nums[i])
        result.append(nums[j])
        i += 1
        j += 1

    return result

# Example usage
nums = [2, 5, 1, 3, 4, 7]
n = 3
result = shuffle(nums, n)
print(result)
