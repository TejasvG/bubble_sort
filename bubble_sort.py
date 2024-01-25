def bubble_sort(arr):
    n = len(arr)
  
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


input_numbers = input("Enter a list of numbers separated by spaces: ")
user_list = list(map(int, input_numbers.split()))


bubble_sort(user_list)


print("Sorted array:", user_list)
