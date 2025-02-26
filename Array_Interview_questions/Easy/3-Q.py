# 3 - Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.


def rotation_arr (arr, d):
    while d > 0:
        reverse_element = arr.pop(0)
        arr.append(reverse_element)
        d -=1
    return arr

arr = list(map(int,input("Enter the array of element : ").split()))
position = int(input("Enter the rotation d positon : "))
print(f"Original array : {arr}")
print(f'Rotated array by {position} position is {rotation_arr(arr, position)}')





'''
Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
Output: {3, 4, 5, 6, 1, 2}
Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

'''


