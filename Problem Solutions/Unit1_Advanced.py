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

def defuse(code, k):
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
                idx = ((i + n) - j) % n
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