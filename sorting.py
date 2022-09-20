print("Brutforce ----selection sort ------")
nums = [1,4,3,5,6,2,9,7]

# def selectionSort(nums):
#     for i in range(len(nums)-1):
#         minvalue = nums[i]
#         index = i
#         for newIndex in range(i+1, len(nums)):
#             if minvalue >nums[newIndex]:
#                 minvalue = nums[newIndex]
#                 index = newIndex
#         nums[i], nums[index] = nums[index], nums[i]
# selectionSort(nums)
# print(nums)

# def bubbleSort(nums):
#     for i in range(2,len(nums)-1):
#         for j in range(len(nums)-i, -1,-1):
#             if nums[j] >nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums
# print(bubbleSort(nums))


# merge sort
# arr1 = [1,2,4,6,9]
# arr2 = [3,5,7,8,10,12]
# def mergeSort(arr1,arr2):
#     # i and j will work as iterator for both lists
#     i,j,= 0,0
#     sorted_arr = []
#     while i <len(arr1) and j <len(arr2):
#         if arr1[i] < arr2[j]:
#             sorted_arr.append(arr1[i])
#             i+=1
#         else:
#             sorted_arr.append(arr2[j])
#             j+=1
#     while i < len(arr1):
#         sorted_arr.append(arr1[i])
#         i+=1
#     while j < len(arr2):
#         sorted_arr.append(arr2[j])
#         j+=1
#     return sorted_arr
# # print(mergeSort(arr1,arr2))

# def devide_and_merge(arr):
#     if len(arr) <2:
#         return arr[:]
#     middle = len(arr)// 2
#     left_side = devide_and_merge(arr[:middle])
#     right_side = devide_and_merge(arr[middle:])
#     return mergeSort(left_side,right_side)
# arr = [1,34,23,45,67,12,32,11,0]
# print(devide_and_merge(arr))

# type 1 lumato
# def quicksort(l1):
#     if len(l1) <2:
#         return l1
#     else:
#         pivot = l1[-1]
#         smaller, equal, larger = [],[],[]
#         for num in l1:
#             if num < pivot:
#                 smaller.append(num)
#             elif num > pivot:
#                 larger.append(num)
#             else:
#                 equal.append(num)
#         print(smaller,equal, larger)
#         print("list", l1)
#         return quicksort(smaller) + equal + quicksort(larger)
# list1 = [2,1,34,56,43,67,10,20,15,42,5]
# print(list1)
# print(quicksort(list1))


# quicksort hoare method
# def swap(a,b,arr):
#     arr[a], arr[b] =arr[b], arr[a]
# def partition(elements,start, end):
#     pivot_index = start
#     pivot= elements[pivot_index]
#     while start <end:
#         while start <len(elements)and elements[start] <= pivot:
#             start +=1
#         while elements[end] > pivot:
#             end -=1
#         if start <end:
#             swap(start, end, elements)
#     swap(pivot_index, end, elements)
#     return end

# def quick_sort(elements, start,end):
#     if start <end:

#         pi = partition(elements,start, end)
#         quick_sort(elements, start, pi-1)
#         quick_sort(elements, pi+1, end)

# elements = [11,9,29, 7,2,15,28]
# quick_sort(elements,0 , len(elements)-1)
# print(elements)


# heap sort algorithm
# def swap(lst, i,j):
#     lst[i], lst[j] = lst[j], lst[i]

# def shiftDown(lst,i, upper):
#     while (True):
#         l, r = i*2+1, i*2+2
#         # upper is the length of list
#         if max(l,r)<upper:
#             if lst[i] >= max(lst[l], lst[r]):
#                 break
#             elif lst[l]> lst[r]:
#                 swap(lst, i, l)
#                 i = l
#             else:
#                 swap(lst,i, r)
#                 i = r
#         elif l<upper:
#             if lst[l]>lst[i]:
#                 swap(lst,i, l)
#                 i = l
#             else:
#                 break
#         elif r<upper:
#             if lst[r]>lst[i]:
#                 swap(lst,i, r)
#                 i = r
#             else:
#                 break
#         else:
#             break
# def heapSort(lst):
#     for j in range ((len(lst)-2)//2,-1,-1):
#         shiftDown(lst, j, len(lst))
#     for end in range(len(lst)-1,0,-1):
#         swap(lst,0,end)
#         shiftDown(lst,0,end)
# elements = [11,9,29, 7,2,15,28]
# heapSort(elements)
# print(elements)

#---------p1 2 sum-------------------#

# def pair_sum_sorted_array(numbers, target):
#     """
#     Args:
#      numbers(list_int32)
#      target(int32)
#     Returns:
#      list_int32
#     """
#     # Write your code here.
#     left = 0
#     right = len(numbers)-1
#     value = False
#     while left < right:
#         left_num = numbers[left]
#         right_num = numbers[right]
#         if left_num+right_num >target:
#             right -=1
#         elif left_num+right_num <target:
#             left +=1
#         else:
#             value = True
#             break
#     if value:
#         return [left,right]
#     return [-1,-1]
