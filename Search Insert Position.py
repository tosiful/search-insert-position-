def find_index(arr, n, K):
	
	
	for i in range(n):
		
		
		if arr[i] == K:
			return i
			
		
		elif arr[i] > K:
			return i
			
	
	return n

arr = [1, 3, 5, 6]
n = len(arr)
K = 5
print(find_index(arr, n, K))
