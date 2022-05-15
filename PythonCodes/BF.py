def minANDmax(arr):
    minimum = int(arr[0])
    maximum = int(arr[0])
    for i in range(len(arr)):
        if int(arr[i]) < minimum:
            minimum = int(arr[i])
        if int(arr[i]) > maximum:
            maximum = int(arr[i])
    return minimum, maximum


if __name__ == '__main__':
    arr = input("Enter the array: ")
    arr = arr.split(', ')
    minimum, maximum = minANDmax(arr)
    print(f"The minimum element of the array is {minimum}")
    print(f"The maximum element of the array is {maximum}")
