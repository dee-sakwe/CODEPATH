print("\nQuestion #4")
'''
Problem 4: Good Samaritan
Superman is doing yet another good deed, using his power of flight to distribute meals for the Metropolis Food Bank. 
He wants to distribute meals in the least number of trips possible.

Metropolis Food Bank currently stores meals in n packs where the ith pack contains meals[i] meals. 
There are also m empty boxes which can contain up to capacity[i] meals.

Given an array meals of length n and capacity of size m, write a function minimum_boxes() 
that returns the minimum number of boxes needed to redistribute the n packs of meals into boxes.

Note that meals from the same pack can be distributed into different boxes.
'''

def minimum_boxes(meals, capacity):
    # total number of boxes required
    result = 0
    # how many total meals we have to share into the capacity boxes
    total_meals = sum(meals)
    # sort capacity in reverse so we start with the biggest containers first
    capacity = sorted(capacity, reverse=True)

    while total_meals > 0:
        # Share the meals into the boxes starting from the largest box
        total_meals -= capacity[result]
        # increment the number of required
        result += 1
    
    return result  # O(nlogn) time because we sort the capacity array


# Example Usage:

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(minimum_boxes(meals, capacity))

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(minimum_boxes(meals, capacity))

'''
Example Output:

2
4
'''

print("\nQuestion #5")
'''
Problem 5: Heist
The legendary outlaw Robin Hood is looking for the target of his next heist. 
Write a function wealthiest_customer() that accepts an m x n 2D integer matrix accounts
where accounts[i][j] is the amount of money the ith customer has in the jth bank. 
Return a list [i, w] where i is the 0-based index of the wealthiest customer and w is the total wealth of the wealthiest customer.

If multiple customers have the highest wealth, return the index of any customer.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.
'''

def wealthiest_customer(accounts: list[list]) -> list:
    # initialize empty array to store the richest person
    richest = [0, 0]

    # traverse through the accounts 
    for index, account in enumerate(accounts):
        # Calculate the wealth of each individual
        wealth = sum(account)

        # Check if current customer is wealthier than the prev richest
        if wealth > richest[1]:
            richest[0], richest[1] = index, wealth

    return richest # O(m * n) time complexity and O(1) space (Output array doesn't count)


# Example Usage:

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
print(wealthiest_customer(accounts))

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
print(wealthiest_customer(accounts))

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
print(wealthiest_customer(accounts))

'''
Example Output:

[0, 6]
[1, 10]
[0, 17]
'''

print("\nQuestion #6")
'''
Problem 6: Smaller Than
Write a function smaller_than_current that accepts a list of integers nums 
and, for each element in the list nums[i], determines the number of other elements in the array that are smaller than it. 
More formally, for each nums[i] count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer as a list.
'''

def smaller_than_current(nums: list) -> list:
    # VER 3: Uses sorting and drops time to O(nlogn)

    # Create a sorted (num, index) pair arrays from nums
    # This allows us to know which numbers are smaller than which
    # I thought of sorting as a possible solution, FTR
    indexed = sorted([(num, i) for i, num in enumerate(nums)])

    n = len(nums)
    result = [0] * n

    # loop through our indexed array. Since it is sorted, the index of the number
    # will also equal the number of elements in nums that are greater than it. Very smart @copilot
    for i, (_, original_index) in enumerate(indexed):
        result[original_index] = i

        # There are times when duplicates exist in nums. We have to account for that
        # run a while loop and check that the number we are dealing with is not the same
        # as the one before it
        while i > 0 and indexed[i][0] == indexed[i - 1][0]:
            # We replace what we originally put as the result with the value of the element before it
            # I originally tried result[original_index] = indexed[i - 1][1]
            result[original_index] = result[indexed[i - 1][1]]  # Copilot actually said result[original_index] = result[indexed[i - 1][1]]
            # Spoiler: he (she? they?) was right.
            # decrement i
            i -= 1

    return result

    """
    # VER 2

    n = len(nums)
    result = [0] * n

    for i in range(n):
        for j in range(n):
            if i != j and nums[j] < nums[i]:
                result[i] += 1

    return result
    """

    '''
	# looks like they are asking for the "brute-force" solution
    # something tells me that using the circular array trick will work here
    n = len(nums)
    # result array of length n
    result = [0] * n

    # for every index in nums
    for i in range(n):
        total = 0
        # we will be checking n - 1 elements to see if they are smaller than the current nums[i]
        for j in range(1, n):
            # if the other numbers are smaller
            if nums[(i + j) % n] < nums[i]:
                total += 1

        # Update our result array at index i with the number of elements in nums greater than nums[i]
        result[i] = total

    return result  # return result array
    # Expected O(n^2) time complexity and O(n) space, although output array isn't usually counted, so maybe O(1) space
    '''


# Example Usage:

nums = [8, 1, 2, 2, 3]
print(smaller_than_current(nums))

nums = [6, 5, 4, 8]
print(smaller_than_current(nums))

nums = [7, 7, 7, 7]
print(smaller_than_current(nums))

# Example Output:

'''
[4, 0, 1, 1, 3]
[2, 1, 0, 3]
[0, 0, 0, 0]
'''

print(f"\nQuestion #7")
'''
Problem 7: Diagonal
Write a function diagonal_sum() that accepts a 2D n x n 
matrix grid and returns the sum of the matrix diagonals. 
Only include the sum of all the elements on the primary diagonal 
and all the elements in the secondary diagonal that are not part of the primary diagonal.

The primary diagonal is all cells in the matrix along a line 
drawn from the top-left cell in the matrix to the bottom-right cell. 
The secondary diagonal is all cells in the matrix along a line 
drawn from the top-right cell in the matrix to the bottom-left cell.
'''

def diagonal_sum(grid: list[list]) -> int:
    # Managed to do it in O(n) time and O(1) space, yay!
    # n being number of rows, obvs

    # keep track of our sum with total initialized to 0
    total = 0
    # number of rows so we don't keep calling len()
    # minor optimization, but worth it still
    n = len(grid)
    # j counter starting from the last index of rows and counting down
    j = n - 1

    # no need to loop if theres only a 1 X 1 matrix
    # dunno if this is strictly necessary tho
    # apparently not lol
    '''
    if n == 1:
        return grid[0][0]
    '''

    # for the total number of rows:
    for i in range(n):
        # elements on the leading diagonal will have the same row number and 
        # column number    
        total += grid[i][i]

        # We don't want to count the middle index in an odd n matrix
        # so we check that i != j
        if i != j:
            total += grid[i][j]

        # decrement j after each run of the loop   
        j -= 1

    return total

    '''
    # first iteration works, but I could probably do it
    # in O(1) extra space (currently O(n) where n is the num of rows)
    total = 0
    seen = set()
    n = len(grid)
    j = n - 1

    if n == 1:
        return grid[0][0]

    for i in range(n):    
        total += grid[i][i]
        seen.add((i, i))
        if (i, j) not in seen:
            total += grid[i][j]
            
        j -= 1

    return total
    '''


'''
Example 1 input matrix with primary and secondary diagonals labelled

Example Usage
'''

grid = [
	[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sum(grid))

grid = [
	[1, 1, 1, 1],
    [1, 1, 1, 1],
	[1, 1, 1, 1],
    [1, 1, 1, 1]
]
print(diagonal_sum(grid))

grid = [
	[5]
]
print(diagonal_sum(grid))
'''
Example Output:

25
8
5
'''

print(f"\nQuestion #8")
'''
QUESTION #8
Batman has a bomb to defuse, and his time is running out! 
His butler, Alfred, is on the phone providing him with a circular array code of length n and key k.

To decrypt the code, Batman must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, write a function decrypt() that returns the decrypted code to defuse the bomb!
'''

def defuse(code: list, k: int) -> list:
    # for easy access
    n = len(code)
    # initialize result array since all the work has to be done simultaneoulsy
    result = [0] * n

    if k > 0:
        # for all chars in the array
        for i in range(n):
            # maintain a total count that is appended to our result array
            # at position i
            total = 0
            # tricky part! Thank you @copilot
            # for the number of chars we are supposed to add
            # e.g if k is 3, we want to add the first, second, and third numbers after code[i]
            for j in range(1, k+1):
                # use the modulo operator to simulate the circular array
                # e.g n = 4, i = 0 , j = 1; idx would be (0 + 1) % 4
                # which would come out to 1
                idx = (i + j) % n
                # so we would add the int at code[idx] to our total
                total += code[idx]

            # add the total sum to result at the index i
            result[i] = total 
    elif k < 0:
        for i in range(n):
            # similar to the case where k is positive
            total = 0
            # had to come up with this by myself, tho lmao
            # really tough
            for j in range(1, abs(k) + 1 ):  # assume k is positive so we know what to add
                # e.g n = 7, k = 3, i = 0, j = [1, 2, 3]
                # i tried to do this by "adding" another array of size n to our input array
                # this allows us to go back without using negative indices, assuming k < n
                # idx = ((0 + 7) - j = 1) % 7
                # idx = (7 - 1) % 7 => 6;
                idx = (i + n - j) % n
                # We then add code[6] to total 
                total += code[idx]

            result[i] = total
    # return result. will return [0] * n if k == 0
    # actually just make code = result and return that
    code = result
    return code


# Example Usage:

code = [5, 7, 1, 4]
k = 3
print(defuse(code, k))

code = [1, 2, 3, 4]
k = 0
print(defuse(code, k))

code = [2, 4, 9, 3]
k = -2
print(defuse(code, k))

'''
Example Output:

[12, 10, 16, 13]
[0, 0, 0, 0]
[12, 5, 6, 13]
'''