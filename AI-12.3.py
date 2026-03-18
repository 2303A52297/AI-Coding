# #generate a code to sort student records(name,roll no,CGPA) CGPA wise in descending order for placement drive using merge sort and quick sort and compare the time taken by both sorting algorithms. compare the performance for large datasets.display top 10 students.
'''import random
import string
import time

# Generate random student data
def generate_students(num_students):
    students = []
    for i in range(num_students):
        name = ''.join(random.choices(string.ascii_uppercase, k=5))
        roll_no = f"R{1000 + i}"
        cgpa = round(random.uniform(5.0, 10.0), 2)
        students.append({'name': name, 'roll_no': roll_no, 'cgpa': cgpa})
    return students

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i]['cgpa'] > R[j]['cgpa']:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort implementation
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]['cgpa']
    i = low - 1
    for j in range(low, high):
        if arr[j]['cgpa'] > pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

# Display top 10 students
def display_top_10(students):
    print(f"{'Rank':<5} {'Name':<8} {'Roll No':<8} {'CGPA':<5}")
    for idx, student in enumerate(students[:10], 1):
        print(f"{idx:<5} {student['name']:<8} {student['roll_no']:<8} {student['cgpa']:<5}")

# Main
if __name__ == "__main__":
    num_students = 100000  # Large dataset
    students = generate_students(num_students)

    # Merge Sort
    students_merge = students.copy()
    start = time.time()
    merge_sort(students_merge)
    merge_time = time.time() - start

    # Quick Sort
    students_quick = students.copy()
    start = time.time()
    quick_sort(students_quick, 0, len(students_quick)-1)
    quick_time = time.time() - start

    print("Top 10 students (Merge Sort):")
    display_top_10(students_merge)
    print("\nTop 10 students (Quick Sort):")
    display_top_10(students_quick)

    print(f"\nTime taken by Merge Sort: {merge_time:.6f} seconds")
    print(f"Time taken by Quick Sort: {quick_time:.6f} seconds")

    if merge_time < quick_time:
        print("Merge Sort is faster for this dataset.")
    elif quick_time < merge_time:
        print("Quick Sort is faster for this dataset.")
    else:
        print("Both algorithms took the same time.")'''

##generate a code to implement bubble sort with ai comments and provide time complexity analysis
'''import random
import string
import time

# Generate random student data
def generate_students(num_students):
    students = []
    for i in range(num_students):
        name = ''.join(random.choices(string.ascii_uppercase, k=5))
        roll_no = f"R{1000 + i}"
        cgpa = round(random.uniform(5.0, 10.0), 2)
        students.append({'name': name, 'roll_no': roll_no, 'cgpa': cgpa})
    return students

# Display top 10 students
def display_top_10(students):
    print(f"{'Rank':<5} {'Name':<8} {'Roll No':<8} {'CGPA':<5}")
    for idx, student in enumerate(students[:10], 1):
        print(f"{idx:<5} {student['name']:<8} {student['roll_no']:<8} {student['cgpa']:<5}")

# Bubble Sort implementation with AI comments and time complexity analysis

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent students by CGPA
            if arr[j]['cgpa'] < arr[j + 1]['cgpa']:
                # Swap if the element found is less than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

    # Time complexity analysis:
    # Best Case: O(n) when the array is already sorted (with optimization)
    # Average and Worst Case: O(n^2) due to nested loops

# Bubble Sort timing and display
if __name__ == "__main__":
    num_students = 1000  # You can adjust this for testing
    students = generate_students(num_students)
    students_bubble = students.copy()
    start = time.time()
    bubble_sort(students_bubble)
    bubble_time = time.time() - start
    print("\nTop 10 students (Bubble Sort):")
    display_top_10(students_bubble)
    print(f"\nTime taken by Bubble Sort: {bubble_time:.6f} seconds")'''



