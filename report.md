Introduction
This report discusses the implementation, analysis, and application of heap data structures. A heap is a specialized binary tree-based data structure that satisfies the heap property. In a max-heap, for every node i, the value of i is greater than or equal to the values of its children. A heap is used in various applications, including Heapsort (a sorting algorithm) and Priority Queues (for scheduling tasks based on priority). This report covers the Heapsort algorithm, its time and space complexity analysis, and compares it with other common sorting algorithms, followed by a discussion of the implementation of a priority queue.

Heapsort Algorithm Implementation
Heapsort Overview
Heapsort is an efficient sorting algorithm based on a binary heap data structure. The core idea is to build a max-heap from the input array and then repeatedly extract the maximum element, placing it at the end of the array. Once the heap is rebuilt, the next maximum element is extracted, and the process continues until the entire array is sorted.

Heapsort Implementation in Python
The Heapsort algorithm can be divided into two main parts:

Building the Max-Heap: We start by converting the input array into a max-heap, where the largest element is at the root. This process is done in O(n) time.
Sorting the Array: After building the heap, we repeatedly swap the root element with the last element in the heap and then heapify the reduced heap. This operation takes O(log n) for each element, leading to a total complexity of O(n log n).
python
Copy code
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
Time Complexity Analysis
Building the Max-Heap: The heapify operation takes O(log n) time for each element, and since we perform it for n/2 elements (the non-leaf nodes), the total time complexity for building the heap is O(n).
Sorting the Array: In the sorting phase, we extract the maximum element (which takes O(log n)) and then rebuild the heap for the remaining elements, which takes O(log n) for each of the n elements. Therefore, the time complexity of sorting is O(n log n).
Space Complexity
Heapsort is an in-place sorting algorithm. It does not require additional storage, as the input array is rearranged in place. The space complexity is therefore O(1).

Priority Queue Implementation
Priority Queue Overview
A priority queue is a data structure that allows for efficient access to the element with the highest or lowest priority. It is commonly implemented using a heap. The PriorityQueue class implements a max-heap where tasks with higher priority are extracted first. Each task is represented by a Task class containing attributes such as task_id, priority, arrival_time, and deadline.

Priority Queue Operations
Insert(Task): Adds a task to the heap while maintaining the heap property. The insertion operation requires O(log n) time due to the need for the heap property to be restored after insertion.
Extract_max(): Removes and returns the task with the highest priority. This operation involves swapping the root element with the last element and then calling heapify to restore the heap property. It also takes O(log n) time.
Increase_key(Task, new_priority): Increases the priority of an existing task and restores the heap property by moving the task up the heap. This operation also takes O(log n) time.
python
Copy code
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent].priority < self.heap[index].priority:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_task = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_task

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def is_empty(self):
        return len(self.heap) == 0
Time Complexity of Priority Queue Operations
Insert: The insert operation requires moving the newly added element up the heap, which takes O(log n) time.
Extract_max: The extract operation requires moving the root element down the heap to restore the heap property, which takes O(log n) time.
Increase_key: The increase operation requires moving the task up the heap, which also takes O(log n) time.
Thus, all major operations in the priority queue take O(log n) time.

Comparison with Other Sorting Algorithms
Heapsort vs. Quicksort
Heapsort has a guaranteed time complexity of O(n log n) in all cases (best, average, and worst), making it more predictable than Quicksort.
Quicksort, on the other hand, has an average-case time complexity of O(n log n) but suffers from a worst-case time complexity of O(n^2) when the pivot is chosen poorly. However, with careful pivot selection (e.g., random pivoting or using the median of three), Quicksort can perform better than Heapsort on average in practice.
Heapsort vs. Merge Sort
Merge Sort also has a guaranteed time complexity of O(n log n) in all cases, but it requires additional memory space of O(n) to store temporary arrays during the merge step, unlike Heapsort, which operates in place with O(1) space complexity.
Heapsort may be more efficient in terms of space since it does not require auxiliary memory, but it often has slightly worse cache performance compared to Merge Sort.
Conclusion
This report discussed the implementation of Heapsort and a priority queue using heaps. Both Heapsort and the priority queue operations exhibit logarithmic complexity, with O(n log n) time complexity for sorting and O(log n) for most priority queue operations. In practice, Heapsort may not be as fast as Quicksort, but it offers consistent performance regardless of input distribution. Merge Sort, while also O(n log n), requires additional space, making Heapsort an attractive option when memory efficiency is crucial.
