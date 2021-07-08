def selection_sort(arr):
	n=len(arr)
	for i in range(n):
		## to store the index of the minimum element
		min_element_index = i
		for j in range(i + 1, n):
			## checking and replacing the minimum element index
			if arr[j] < arr[min_element_index]:
				min_element_index = j
		## swaping the current element with minimum element
		arr[i], arr[min_element_index] = arr[min_element_index], arr[i]
	return arr
