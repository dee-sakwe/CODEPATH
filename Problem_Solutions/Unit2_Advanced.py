'''
Problem 2: Pirate Message Check
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. 
She will know she can trust the message if it contains all of the letters in the alphabet.
Given a string message containing only lowercase English letters and whitespace, 
write a function can_trust_message() 
that returns True if the message contains every letter of the English alphabet at least once,
and False otherwise.

# Understand: Check that message contains every letter in the alphabet

# Plan: Krish - Create a dict with letters of the alphabet as keys. increment the val if the 
# exists at least once

# Frankelly - 
'''

def can_trust_message(message):
    
    # initialize dict
    alpha = {}

    # iterate through message
    for char in message:
        # check if char is an alphabet and if it is in alpha 
            if char.isalpha():
                # increment the value of alpha[char]
                alpha[char] = alpha.get(char, 0) + 1

    # returns true if len(alpha.keys()) == 26 else false
    return len(alpha.keys()) == 26
    '''


    # We could use sets
    seen = set()

    # for char in messages check if it is an alphabet and then add to seen
    for char in message:
        if char.isalpha():
            seen.add(char)

    # returns true if len(alpha.keys()) == 26 else false
    return len(seen) == 26  # O(n) time complexity
    '''
    

'''
Example Usage:
'''

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))

'''
# Example Output:

True
False
'''