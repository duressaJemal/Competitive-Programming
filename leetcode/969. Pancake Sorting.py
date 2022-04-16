class Solution:
    def pancakeSort(self, arr):

        output = []
        #find index of the largest element
        def largest(arr):
            largest = 0
            for i in range(len(arr)):
                if arr[i] > arr[largest]:
                    largest = i
            return largest
            
        # flip
        def flip(arr, largest):
            output.append(largest + 1)
            i = 0
            while largest > i:
                arr[i], arr[largest] = arr[largest], arr[i]
                i += 1
                largest -= 1
            return arr

        current_index = len(arr)-1
        while current_index > 0:
            largest_index = largest(arr[:current_index + 1])

            if largest_index == current_index:
                current_index -= 1
                continue

            if largest_index != 0:
                flip(arr, largest_index)
            flip(arr, current_index)
            current_index -= 1

        return output
