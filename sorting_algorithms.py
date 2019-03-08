import time
import random

class SortingAlgorithms(object):
    """
    Basic sorting algorithms for one-dimensional lists,
    as specified by Introduction to Algorithms by Thomas H. Cormen.
    Pseudocode translated to Python by Ravi Jotwani.
    """

    def insertion_sort(self, A):
        """
        Sorts a list in-place by inserting the first unsorted element
        into the set of sorted elements.
        􏰥Worst-case runtime analysis: ϴ(n²)
        """
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while i > -1 and A[i] > key:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = key

    def merge_sort(self, A):
        """
        Sorts a list in-place by inserting the first unsorted element
        into the set of sorted elements.
        􏰥Worst-case runtime analysis: ϴ(n)
        """
        if len(A) > 1:
            q = len(A)//2
            L, R = A[:q], A[q:]
            self.merge_sort(L)
            self.merge_sort(R)
            i, j, k = 0, 0, 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                A[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                A[k] = R[j]
                j += 1
                k += 1

    def analyze_runtime(self):
        """
        Analyzes runtime of various sorting algorithms.
        """
        self.analyze_insertion_sort(100000, 50)
        self.analyze_merge_sort(100000, 50)

    def analyze_insertion_sort(self, num_trials, list_size):
        """
        Analyzes runtime of insertion sort.
        """
        print('Running ' + str(num_trials) + ' tests on insertion sort')
        print('List size: ' + str(list_size) + '\n')
        results = []
        for i in range(num_trials):
            A = []
            for j in range(list_size):
                A.append(random.random())
            t0 = time.time()
            self.insertion_sort(A)
            t1 = time.time()
            results.append(t1 - t0)
        print('min: ' + str(round(min(results) * 1000, 5)) + 'ms')
        print('avg: ' + str(round(sum(results) * 1000 / num_trials, 5)) + 'ms')
        print('max: ' + str(round(max(results) * 1000, 5)) + 'ms\n')

    def analyze_merge_sort(self, num_trials, list_size):
        """
        Analyzes runtime of merge sort.
        """
        print('Running ' + str(num_trials) + ' tests on merge sort')
        print('List size: ' + str(list_size) + '\n')
        results = []
        for i in range(num_trials):
            A = []
            for j in range(list_size):
                A.append(random.random())
            t0 = time.time()
            self.merge_sort(A)
            t1 = time.time()
            results.append(t1 - t0)
        print('min: ' + str(round(min(results) * 1000, 5)) + 'ms')
        print('avg: ' + str(round(sum(results) * 1000 / num_trials, 5)) + 'ms')
        print('max: ' + str(round(max(results) * 1000, 5)) + 'ms\n')


sa = SortingAlgorithms()
sa.analyze_runtime()
