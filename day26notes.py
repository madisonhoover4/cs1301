# Day 26 Notes

'''

Computation Complexity- measuring the efficiency of an algorithm in terms of..
space(memory) and time(speed)

Big-O notation -- O(f(n))
the big O is different based on the number of items you're looking at

for num1 in range(0,n):
    for num2 in range(0,n):
        x = x+1


every time you have a loop within a loop, the big O is n^2 aka O(n*n) = O(n^2)
constants don't matter, aka (0, 25n) is same as (0, n) for big O

O(1) - program always takes same amount of time, regardless of data
    # ex. looking for smallest item in a sorted list
    # called constant time

O(n) - program gets slower in proportion to the amt of data in elements n
    # called linear time
    # ex. searching for something and you have to look at every item

O(n^2) - program gets slower as a square of the amount of data elements n
    # quadratic time
    # ex. loop inside a loop

O(n*log(n)) - the program gets slower as a bit bigger than linear growth in n
    # CS always uses log base 2
    # ex. loop within a loop (but one goes thru all items, other only thru...
    log of the items
    # one loop only has log n occurrences
    # base 2 logarithms are dividing by half each iteration


O(logn) - Binary Search - divide and conquer (EFFICIENT)

O(n) - Sequential Search - look at all words in a dictionary (INEFFICIENT)
    # best case O(1) first word
    # worst case O(n) not in there
    # average case O(n/2)

    
    














'''
