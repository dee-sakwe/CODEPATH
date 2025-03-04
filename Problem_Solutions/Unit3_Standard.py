# SESSION 1




# Get this out of the way fr
from collections import deque


print("Question #1")
'''
Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. 
Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. 
You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.

This question may be answered using a stack, which is a new data structure. 
To learn more about stacks and how to use them in Python, 
check out the unit cheatsheet or use a search engine or generative AI tool to conduct your own research.

Initialize a stack to keep track of the opening tags as you encounter them.
Iterate through the posts
If it's an opening tag, push it onto the stack
If it's a closing tag, check if the stack is not empty and whether the tag at the top of the stack is the corresponding opening tag
If yes, pop the opening tag from the stack (we've found its match!)
If no, the tags are not properly nested and we should return False
After processing all characters, if the stack is empty, all tags were properly nested and we should return True. 
If the stack is not empty, some opening tags were not closed, so return False
'''

def is_valid_post_format(posts):
    # This is essentialy the valid parenthesis question with extra steps
    # we want to use a stack to ensure that open pars match close par
    # we can map close par to open par using a hashmap

    match = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    # initialize a stack 
    stack = []

    # In one passthrough, go through our posts and add open par to the stack
    # if we come across a close par, check that the top element on the stack is the matching
    # open par and then pop if it is. Else we can straight return False.

    for par in posts:
        # Check that the par is an open par, and then add it to our stack
        if par in "({[":
            stack.append(par)

        else:
            if stack and stack[-1] == match[par]:
                stack.pop()
            else:
                return False

    # We can return true if our stack is empty else False
    return not stack

# Example Usage:

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

"""
Example Output:

True
True
False
"""


print("\nQuestion #2")
"""
On your platform, comments on posts are displayed in the order they are received. 
However, for a special feature, you need to reverse the order of comments before displaying them. 
Given a queue of comments represented as a list of strings, reverse the order using a stack.
"""

def reverse_comments_queue(comments):
    """
    # I could use reversed to quickly get the result
    return [x for x in reversed(comments)]  # This is not what is needed, but it's a line of code that works
    """

    # Pretty straight forward. We want to create a stack and pop from it onto an output array
    # I'm going to assume the input queue is a stack just for speed sake
    result = []

    # do it as many times as there are comments in our queue
    for i in range(len(comments)):
        result.append(comments.pop())  # pop our "stack" and append to the output list

    # return our result after looping. O(n) time, O(n) space
    return result

# Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

"""
Example Output:

['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']

"""


print("\nQuestion #3")
"""
Problem 3: Check Symmetry in Post Titles
As part of a new feature on your social media platform, 
you want to highlight post titles that are symmetrical,
meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. 
Given a post title as a string, use a new algorithmic technique 
the two-pointer method to determine if the title is symmetrical.
"""

def is_symmetrical_title(title: str) -> bool:
    n = len(title)
    # initialize two pointers
    left = 0
    right = len(title) - 1

    # bring our pointers towards each other
    while left <= right:
        # move left to the right if we come across a space char
        while left <= right and not title[left].isalnum():
            left += 1
        # move right to the left if we come across a space char
        while left <= right and not title[right].isalnum():
            right -= 1

        if left > right:
            break

        # return False if the chars don't match
        if title[left].lower() != title[right].lower():
            return False
        
        # increment left and decrement right if they do match
        left += 1
        right -= 1

    # return True if the loop finishes
    return True  # O(n) time, O(1) space


# Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))
print(is_symmetrical_title("W   hatsapp D a v i d   divadPPastah w   "))

""" 
Example Output:

True
False
True
"""


print("\nQuestion #4")
"""
Problem 4: Engagement Boost
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. 
To analyze the impact of certain strategies, you decide to square each engagement rate 
and then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
"""

def engagement_boost(engagements: list) -> list:
    n = len(engagements)
    # initialize an empty array to store all squared engagements
    result = [0] * n
    # two pointers technique
    left = 0
    right = len(engagements) - 1
    pos = n - 1


    while left <= right:  # While left has not surpassed right
        # We compare the squares of the extremes. They will produce the largest squares
        square_left, square_right = engagements[left] ** 2, engagements[right] ** 2
        if square_left >= square_right:
            # if the square of the num at the left index is greater
            # add that to our result array and increment left
            result[pos] = square_left
            left += 1
            pos -= 1
        else:
            # else append the square of the num at the right index
            # and decrement right
            result[pos] = square_right
            right -= 1
            pos -= 1

        
    # return the reversed array
    return result # O(n) time, O(1) space (Don't count output array)


# Example Usage:

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

""" 
Example Output:

[0, 1, 9, 16, 100]
[4, 9, 9, 49, 121]
"""


print("\nQuestion #5")
"""
Problem 5: Content Cleaner
You want to make sure your posts are clean and professional. 
Given a string post of lowercase and uppercase English letters, 
you want to remove any pairs of adjacent characters where one is the lowercase version of a letter 
and the other is the uppercase version of the same letter. 
Keep removing such pairs until the post is clean.

A clean post does not have two adjacent characters post[i] and post[i + 1] where:

post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.

Note that an empty string is also considered clean.
"""

def clean_post(post: str) -> str:
    # This problem can be solved using a stack
    stack = []

    # We iterate through post. We check if the current char is the same as the top
    # of our stack. If so, we pop our stack, else we add the char to the top of the stack
    for char in post:
        # check that stack is non-empty and that the current char is the same as the
        # char on top of stack
        if stack and stack[-1].lower() == char.lower():
            # check that char and stack[-1] are opposites in terms of case
            if (char.islower() and stack[-1].isupper()) or (char.isupper() and stack[-1].islower()):
                # pop the top character off of stack
                stack.pop()
            # else they are both lowercase and there's no need to remove them
            else:
                # add the char to the top of the stack
                stack.append(char)

        # add char to our stack 
        else:
            stack.append(char)

    # join the remnants of the stack and return the resultant string
    return "".join(stack)  # O(n) time, O(n) space (stack data structure)

# Example Usage:

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s"))
print(clean_post("aAAA posttT")) 

""" 
Example Output:

post

s
"""


print("\nQuestion #6")
"""
Problem 6: Post Editor
You want to add a creative twist to your posts by reversing the order of characters in each word within your post 
while still preserving whitespace and the initial word order. 
Given a string post, use a queue to reverse the order of characters in each word within the sentence.
"""

def edit_post(post: str) -> str:
    result = []

    for word in post.split():
        result.append("".join(reversed(word)))

    return " ".join(result)

    '''
    # Stack solution (Could have been queue too)

    words = post.split()
    result = []

    for word in words:
        stack = []
        for char in word:
            stack.append(char)
        
        temp = []
        while stack:
            temp.append(stack.pop())

        result.append("".join(temp))

    return " ".join(result)
    '''

# Example Usage:

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 

""" 
Example Output:

tsooB ruoy tnemegegna htiw eseht spit
kcehC tuo ym tseval golv
"""