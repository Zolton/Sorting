# Iterative Sorting Algorithms

## Insertion Sort
Think back to class or team picture day. Everyone stands in a line facing the photographer. Starting at the left-hand side of the line, the photographer checks to make sure each person is taller than the person next to them. If they are shorter, the photographer pulls them out and shifts people over to the right until he or she finds the right spot for this person. They then insert them back into the line. This process repeats until the photographer reaches the last person on the right-hand side, who must be the tallest person in the group. This is ***Insertion Sort***.

[(VIDEO) Insert-sort with Romanian folk dance](https://www.youtube.com/watch?v=ROalU379l3U) 

[![(VIDEO) Insert-sort with Romanian folk dance](https://i.ytimg.com/vi/ROalU379l3U/hqdefault.jpg)](https://www.youtube.com/watch?v=ROalU379l3U) 


### Algorithm
1. Separate the first element from the rest of the array. Think about it as a sorted list of one element.

2. For all other indices, beginning with [1]:

    a. Copy the item at that index into a temp variable

    b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted  
    - Shift items over to the right as you iterate
    
    c. When the correct index is found, copy temp into this position


### Your Task
- Implement the `insertion_sort()` function in the Guided Project with your TA


### Real-World Applications
The answer to the question, "Is ***Insertion Sort*** an efficient algorithm?" is not always the same. The runtime of ***Insertion Sort*** is dependent on how close to being "in-order" the data is to begin with. In a scenario where you are performing ***Insertion Sort*** on an already or mostly sorted array, very few elements will need to be shifted over, leading to a runtime of Ω(n). However, in a worse-case scenario, where the maximum number of shifts are being performed, the runtime of this algorithm is O(n²).


## Bubble Sort
In **Bubble Sort**, we make a series of swaps between adjacent elements, gradually moving larger elements towards the end of the array (or _bubbling_ larger elements up).

### Algorithm
1. Loop through your array
    - Compare each element to its neighbor
    - If elements in wrong position (relative to each other, swap them)
2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

### Real-World Applications
***Bubble Sort*** is not ideal for many real-world applications. If a small element that _should_ be at the beginning of our array is originally located near the end, it will take a long time to move it into its correct position.

However, it should be noted that if you perform **Bubble Sort** on an array that's already sorted, it will only require a single pass through the array, making its best-case performance linear. It's also very simple to implement.

### Your Task
- Complete `bubble_sort()` in `iterative_sorting.py`.


## Selection Sort
***Selection Sort*** is an algorithm that many of you have probably used before when sorting things in your everyday lives. Imagine that you have several books you want to arrange on a shelf from shortest to tallest. You start off by looking for the shortest book, and when you find it, put it on the far left side of the shelf. Then, you look for the second shortest book and insert it directly to the right of the first book. You repeat this process, selecting the next shortest book and moving it next to the most recently placed book, until you have moved all books into the correct place. This is ***Selection Sort***.  

An example of this algorithm being applied to an array with 10 numerical elements can be seen in the video below.

[(VIDEO) Select-sort with Gypsy folk dance](https://www.youtube.com/watch?v=Ns4TPTC8whw)

[![(VIDEO) Select-sort with Gypsy folk dance](https://i.ytimg.com/vi/Ns4TPTC8whw/hqdefault.jpg)](https://www.youtube.com/watch?v=Ns4TPTC8whw)

### Algorithm
1. Start with current index = 0

2. For all indices EXCEPT the last index:

    a. Loop through elements on right-hand-side 
    of current index and find the smallest element

    b. Swap the element at current index with the
    smallest element found in above loop


### Real-World Applications
While ***Selection Sort*** is one of the easier sorting algorithms to understand and implement, it has one major drawback - its efficiency.

Recall that the runtime complexity of an algorithm, often expressed using *Big O notation*, tells us how the amount of operations our algorithm requires will grow as the size of our input grows. ***Selection Sort*** has  a runtime of O(n²), making it impractical to use with many large, real-world data sets.

### Your Task
- Complete the missing parts of `selection_sort()` in `iterative_sorting.py`.

## TO-DO in iterative_sorting.py
- Complete `selection_sort()` and `bubble_sort()`

## Stretch Goals

### Try to write a search function
- Complete the functions in `searching.py`

### There are a few "order n" sorting algorithms whose runtime will be linear, even in a worst case scenario. 
Look into Counting Sort.
- How is this algorithm different from other iterative sorting algorithms?
    - What are the advantages/disadvantages to this type of sorting algorithm?
- Take a look a the pseudocode for this algorithm and try implementing it in Python.

### You Might be Surprised at What Passes for a Sorting Algorithm
- Explore Bogo Sort and summarize how it works in a couple of sentences.
